
# 🤖 VIORA: A Vision-Enabled Multimodal AI Agent

> Build your own intelligent, witty AI assistant that **sees**, **listens** and **responds** like a human using cutting-edge open-source tools.


## 🚀 Overview

**Dora** is a multimodal AI assistant that combines **voice**, **vision**, and **text** to deliver natural, interactive experiences using agentic workflows. Inspired by Gemini Live and powered by tools like LangGraph, Whisper, Groq, and ElevenLabs, Dora is capable of:

- Understanding spoken queries via **real-time transcription**
- Analyzing **live webcam feed** to answer visual questions
- Deciding when to **invoke tools intelligently** (ReAct agent)
- Responding with **human-like speech** using text-to-speech models

> ⚡️ All in one Python project. No proprietary black-boxes. 100% customizable. 100% free.

---

## 🧠 Features

- 🔁 **Agentic AI Workflow**: Built using LangGraph & ReAct pattern
- 🎤 **Voice Input (Speech-to-Text)**: Powered by OpenAI Whisper
- 👁️ **Vision Input (Webcam + OpenCV)**: Real-time image analysis
- 📣 **Voice Output (Text-to-Speech)**: Supports both ElevenLabs and G-TTS
- 🧩 **Smart Tool Calling**: Dynamically calls tools only when needed
- 🌐 **Groq + Meta LLaMA 4 Vision Model**: For multimodal reasoning
- 💻 **Frontend via Gradio**: Seamless live interaction UI

---

## 🧰 Tech Stack

| Component             | Tool/Library         |
|-----------------------|----------------------|
| Language Model        | Gemini 1.5 (Google), Groq, Claude (Optional) |
| Agent Framework       | LangChain + LangGraph |
| Vision Capture        | OpenCV               |
| Speech-to-Text        | OpenAI Whisper       |
| Text-to-Speech        | ElevenLabs / G-TTS   |
| Frontend UI           | Gradio               |
| Audio Processing      | PyDub, PortAudio     |

---

## 📦 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/sai-charan1/VIORA.git
````

### 2. Create Virtual Environment

```bash
uv venv .
uv pip install -r requirements.txt
```

### 3. Environment Variables (`.env`)

Create a `.env` file in the root with the following keys:

```env
GROQ_API_KEY=your_groq_key
GOOGLE_API_KEY=your_google_gemini_key
ELEVENLABS_API_KEY=your_elevenlabs_key
```

### 4. Run the App

```bash
# Phase 1 - Set up tool & agent
uv run ai_agent.py

# Phase 2 - Enable speech input
uv run speech_to_text.py

# Phase 3 - Launch front-end
uv run app.py
```

---

## 🖼️ Architecture

```
User Voice/Input
     ↓
Speech-to-Text (Whisper)
     ↓
  LangGraph Agent  ──────▶ Tool Call (if needed: Vision, Web Search, etc.)
     ↓                        ↓
Text Response        Webcam Image / Groq LLaMA Vision Model
     ↓                        ↓
Text-to-Speech (11Labs / G-TTS)
     ↓
Gradio Frontend Output
```

---

## 📸 Example Queries

| Query                            | Input Type | Response Example                          |
| -------------------------------- | ---------- | ----------------------------------------- |
| "What color shirt am I wearing?" | Vision     | "Looks like you’re wearing a black shirt" |
| "Do I have a spect?"             | Vision     | "Yes!"                                    |
| "What is 5 + 2?"                 | Text only  | "That's an easy one — 7!"                 |
| "Who is the PM of India?"        | Web        | "As of 2025, it's Narendra Modi."         |

---

## 📁 Folder Structure

```
📦VIORA
 ┣ 📜ai_agent.py            # LangGraph-based AI agent
 ┣ 📜tools.py               # Tool functions (vision, Groq, etc.)
 ┣ 📜speech_to_text.py      # Whisper integration
 ┣ 📜text_to_speech.py      # 11Labs/G-TTS output
 ┣ 📜app.py                 # Gradio front-end
 ┣ 📜.env                   # Environment keys
 ┗ 📜README.md              # You're here
```

---

## 🧪 TODO / Future Enhancements

* [ ] Add memory/chaining with LangChain
* [ ] Add internet search (Bing tool or Serper.dev)
* [ ] Docker support
* [ ] Add streaming voice responses
* [ ] Deploy on Hugging Face Spaces or Streamlit Cloud

---

## 🤝 Contributing

Open to pull requests! Feel free to fork and improve the project.

---

## 📄 License

MIT License

---

## 📢 Acknowledgments

* Inspired by Google Gemini Live
---
