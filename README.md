#  LiveKit LLM Voice Agent

This project demonstrates real-time audio streaming, intelligent LLM-based response generation, interruption handling, and modular production architecture using Python.

---

#  Features

- Real-time audio streaming via LiveKit (WebRTC)
- Voice Activity Detection (WebRTC VAD)
- Streaming Speech-to-Text (Google Cloud)
- LLM-powered contextual responses (OpenAI GPT)
- Text-to-Speech synthesis (Google Cloud)
- Conversation memory (short-term context retention)
- Interruption handling (user can stop bot mid-response)
- Silence detection with reminder prompt
- Docker-ready deployment

---

#  Architecture Overview

User Speech  
→ LiveKit Audio Track  
→ Voice Activity Detection (VAD)  
→ Google Speech-to-Text  
→ OpenAI GPT (LLM)  
→ Google Text-to-Speech  
→ LiveKit Audio Output  

---

# Setup Instructions

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/livekit-llm-voice-agent.git
cd livekit-llm-voice-agent

## 2️⃣ Create Virtual Environment (Recommended)
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

## 3️⃣ Install Dependencies
pip install -r requirements.txt

##4️⃣ Configure Environment Variables
Create a .env file in the root directory.
Use .env.example as reference.

## Required Environment Variables

Create a .env file with the following:

LIVEKIT_URL=
LIVEKIT_API_KEY=
LIVEKIT_API_SECRET=

OPENAI_API_KEY=

GOOGLE_APPLICATION_CREDENTIALS=/absolute/path/to/gcloud.json

##▶️ How to Run

After setting environment variables:

python app/main.py

The bot will:

Connect to LiveKit room

Listen to user speech

Convert speech to text

Generate intelligent response using GPT

Convert response to speech

Play audio back into the room

##  Run with Docker (Optional)
docker build -t voice-agent .
docker run --env-file .env voice-agent

##📦 SDKs & Libraries Used
Core SDKs

LiveKit Python SDK – Real-time WebRTC audio streaming

OpenAI Python SDK – GPT LLM integration

Google Cloud Speech SDK – Streaming Speech-to-Text

Google Cloud Text-to-Speech SDK – Audio response synthesis

WebRTC VAD (webrtcvad) – Voice activity detection

Supporting Libraries

numpy

structlog

python-dotenv

asyncio

##  External Services Used

This project depends on the following external services:

LiveKit Server

Handles real-time WebRTC communication

OpenAI API

Generates intelligent conversational responses

Google Cloud Speech-to-Text

Converts speech audio to text

Google Cloud Text-to-Speech

Converts LLM response text into audio

These services require valid API credentials.

##  Known Limitations

Short-term memory only (last ~10 conversation turns)

No persistent database storage

Single-room / single-session oriented

Not optimized for ultra-low latency streaming yet

No authentication layer for participants

No horizontal scaling configuration (requires Kubernetes for production scale)

Basic silence detection (not ML-based endpoint detection)

## Future Improvements

Redis-backed conversation memory

RAG (Retrieval Augmented Generation)

Streaming LLM response playback

Multi-user room support

Prometheus metrics & observability

Kubernetes deployment

Speaker diarization

Emotion-aware conversational prompting