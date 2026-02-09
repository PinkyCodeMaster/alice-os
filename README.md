# Alice OS

> **"Alexa alternative built for one person — me."**

A sovereign, deeply-personal AI assistant that knows your life intimately and proactively helps you live better. 100% local. No cloud. No big tech.

---

## 🎯 The Vision

Alice OS is not just a voice assistant. It's a **personal AI operating system** that:

### Knows You Deeply
- **Where you are** — Location awareness, room detection
- **What you're doing** — Activity recognition, context
- **How you're doing it** — Mood, energy, focus levels
- **When you're doing it** — Time patterns, routines

### Helps You Live Better
- 🏠 **Smart Home Control** — Matter/Thread, fully local
- 💰 **Finances** — Budget tracking, spending insights, savings goals
- 🛒 **Shopping** — Auto-reorder, price tracking, pantry management
- 🔄 **Habit Formation** — Break bad habits, build good ones
- 📚 **Learning** — Course tracking (TM129!), spaced repetition
- ⏰ **Productivity** — Context-aware reminders, focus sessions
- ❤️ **Health & Wellbeing** — Sleep, exercise, mood tracking

---

## Why Alice OS?

| Feature | Alexa/Google Home | Alice OS |
|---------|------------------|----------|
| 100% Local | ❌ Cloud required | ✅ Runs offline |
| Your Data | 📡 Sent to servers | 🔒 Never leaves your network |
| Custom Voice | ❌ Generic | ✅ Deanna's voice |
| Knows Your Habits | ❌ No | ✅ Learns & adapts |
| Proactive Help | ⚠️ Limited | ✅ Deeply personalized |
| Customizable | ❌ Locked down | ✅ Open source |

---

## 🏗️ Architecture

### Core Stack
- **Voice Input:** Whisper (local STT)
- **Brain:** Ollama/llama.cpp (local LLM)
- **Voice Output:** Piper TTS (custom Deanna voice)
- **Orchestration:** Python

### Entry Points
- 📱 **Mobile App** — React Native (away from home)
- 🎤 **RPi Device** — Alexa-style always-listening device
- 💻 **PC App** — Deep integration with your computer

### Smart Home
- **Matter/Thread** protocol for local device control
- No cloud dependencies for automations

---

## 📋 Current Focus (Phase 0)

- ✅ Ubuntu VM ready
- ⏳ Piper TTS + Deanna voice (recording soon!)
- ⏳ Python + Whisper + Ollama setup
- ⏳ Basic voice loop (voice → text → LLM → voice)

---

## 🚀 Getting Started

```bash
# Clone
git clone https://github.com/PinkyCodeMaster/alice-os.git
cd alice-os

# Run locally
python -m alice_os
```

---

## 📁 Project Structure

```
alice-os/
├── .github/workflows/     # CI/CD pipeline
├── alice_os/              # Core modules
│   ├── voice/            # Whisper + Piper
│   ├── brain/            # Ollama integration
│   ├── home/             # Smart home control
│   ├── habits/           # Habit tracking
│   ├── finance/          # Budget & spending
│   └── context/          # Location, activity, mood
├── mobile/               # React Native app
├── device/               # RPi Alexa alternative
└── tests/                # Test suite
```

---

## 🤝 Contributing

This is a personal project, but PRs welcome. Focus on:
- Privacy-first architecture
- Local-only operation
- Proactive AI features

---

## 📜 License

MIT — Build it, break it, make it yours.

---

**Built by Pinky with ❤️**
*"Alice, who are you?" → "I am Alice. I am here to help."*
