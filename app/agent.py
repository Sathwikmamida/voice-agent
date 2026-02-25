import asyncio
import time
from livekit import rtc
from config import SAMPLE_RATE, SILENCE_TIMEOUT
from vad import VoiceActivityDetector
from stt import StreamingSTT
from tts import TTS
from memory import ConversationMemory
from llm import LLM


class VoiceAgent:
    def __init__(self, room):
        self.room = room
        self.vad = VoiceActivityDetector()
        self.stt = StreamingSTT(SAMPLE_RATE)
        self.tts = TTS()
        self.memory = ConversationMemory()
        self.llm = LLM()

        self.last_speech_time = time.time()
        self.is_speaking = False

    async def handle_audio(self, track):
        audio_stream = rtc.AudioStream(track)
        buffer = bytearray()

        async for frame in audio_stream:
            pcm = frame.data

            # Detect speech
            if self.vad.is_speech(pcm, SAMPLE_RATE):
                self.last_speech_time = time.time()
                buffer.extend(pcm)

                # Interrupt if user speaks while bot speaking
                if self.is_speaking:
                    self.is_speaking = False

            # If silence after speech -> process
            elif buffer and not self.is_speaking:
                self.is_speaking = True

                transcript = self.stt.transcribe_stream([bytes(buffer)])
                buffer.clear()

                if transcript:
                    await self.process_transcript(transcript)

                self.is_speaking = False

            # Silence reminder
            if time.time() - self.last_speech_time > SILENCE_TIMEOUT:
                await self.respond("Are you still there?")
                self.last_speech_time = time.time()

    async def process_transcript(self, transcript: str):
        self.memory.add_user(transcript)

        reply = self.llm.generate(self.memory.get_context())

        self.memory.add_assistant(reply)

        await self.respond(reply)

    async def respond(self, text: str):
        audio_data = self.tts.synthesize(text)

        source = rtc.AudioSource(SAMPLE_RATE, 1)
        await self.room.local_participant.publish_audio_track(
            "bot-audio",
            source
        )

        source.capture_frame(audio_data)