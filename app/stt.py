from google.cloud import speech


class StreamingSTT:
    def __init__(self, sample_rate: int):
        self.client = speech.SpeechClient()
        self.sample_rate = sample_rate

    def transcribe_stream(self, audio_chunks):
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=self.sample_rate,
            language_code="en-US",
        )

        streaming_config = speech.StreamingRecognitionConfig(
            config=config,
            interim_results=False
        )

        requests = (
            speech.StreamingRecognizeRequest(audio_content=chunk)
            for chunk in audio_chunks
        )

        responses = self.client.streaming_recognize(
            streaming_config, requests
        )

        for response in responses:
            for result in response.results:
                if result.is_final:
                    return result.alternatives[0].transcript

        return ""