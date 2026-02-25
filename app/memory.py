class ConversationMemory:
    def __init__(self):
        self.history = [
            {
                "role": "system",
                "content": "You are a helpful real-time AI voice assistant."
            }
        ]

    def add_user(self, text: str):
        self.history.append({"role": "user", "content": text})

    def add_assistant(self, text: str):
        self.history.append({"role": "assistant", "content": text})

    def get_context(self):
        # Keep last 10 messages to avoid token overflow
        return self.history[-10:]