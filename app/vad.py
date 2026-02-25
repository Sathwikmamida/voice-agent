import webrtcvad


class VoiceActivityDetector:
    def __init__(self, aggressiveness=2):
        self.vad = webrtcvad.Vad(aggressiveness)

    def is_speech(self, frame: bytes, sample_rate: int) -> bool:
        try:
            return self.vad.is_speech(frame, sample_rate)
        except Exception:
            return False