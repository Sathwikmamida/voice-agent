import asyncio
from livekit import rtc
from config import LIVEKIT_URL, LIVEKIT_API_KEY, LIVEKIT_API_SECRET
from agent import VoiceAgent


async def main():
    room = rtc.Room()

    token = rtc.AccessToken(
        LIVEKIT_API_KEY,
        LIVEKIT_API_SECRET
    ).to_jwt()

    await room.connect(LIVEKIT_URL, token)

    print("Voice Agent connected to LiveKit room")

    agent = VoiceAgent(room)

    @room.on("track_subscribed")
    async def on_track(track, publication, participant):
        if track.kind == rtc.TrackKind.KIND_AUDIO:
            await agent.handle_audio(track)

    await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())