# 🎙 LiveKit LLM Voice Agent

A production-ready real-time AI voice assistant built using:

- LiveKit (WebRTC)
- Google Speech-to-Text (Streaming)
- OpenAI GPT (LLM)
- Google Text-to-Speech
- WebRTC VAD
- Async Python Architecture

---

## 🚀 Features

- Real-time audio streaming
- Voice Activity Detection (WebRTC VAD)
- Streaming Speech Recognition
- LLM-powered contextual responses
- Conversation memory (short-term)
- Interruption handling
- Silence detection reminder
- Docker support
- Modular architecture

---

## 🏗 Architecture

User Speech  
→ LiveKit Audio  
→ VAD  
→ Google STT  
→ GPT (LLM)  
→ Google TTS  
→ LiveKit Audio Output  

---

## ⚙️ Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/livekit-llm-voice-agent.git
cd livekit-llm-voice-agent