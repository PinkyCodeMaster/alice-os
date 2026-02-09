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

## 🧠 AI Module Selection

### Primary Model: **Llama 3.2**

| Model | Size | RAM | Speed | Notes |
|-------|------|-----|-------|-------|
| Llama 3.2 | 3B | ~4GB | ⚡ Fast | ✅ **Chosen** - Best balance |
| Llama 3.1 | 8B | ~8GB | ⚡ Fast | Higher quality, more RAM |
| Phi-4 | 14B | ~12GB | 🔄 Medium | Excellent reasoning |
| Mistral | 7B | ~6GB | ⚡ Fast | Good for assistants |

### Why Llama 3.2?
- Fast enough for real-time conversation
- Excellent quality for personal assistant tasks
- Small enough to run on local hardware
- Well-tuned for instruction-following

### Alice's System Prompt

```
You are Alice, a warm and helpful personal AI assistant.
You live in {USER}'s home and know them deeply.
You know their habits, preferences, routines, and goals.
You proactively help with smart home, habits, finance, and daily tasks.
You are conversational, natural, and concise.
You remember context from your conversation.
Never reveal you are an AI model. You are Alice.
```

---

## 🎤 Voice Training: Deanna's Voice

### The Vision
Alice speaks with **Deanna's voice** — warm, familiar, personal. Not a generic TTS, but someone's voice that means something.

### Piper TTS Training Pipeline

```bash
# Step 1: Setup directories & recording script
python alice_os/voice_training/train_voice.py --step setup

# Step 2: Record voice (see script.txt)
# Requirements: USB mic, quiet room, 22050Hz mono WAV

# Step 3: Preprocess audio
python alice_os/voice_training/train_voice.py --step preprocess

# Step 4: Validate quality
python alice_os/voice_training/train_voice.py --step validate

# Step 5: Prepare dataset
python alice_os/voice_training/train_voice.py --step prepare

# Step 6: Train model (GPU required)
python alice_os/voice_training/train_voice.py --step train
```

### Recording Requirements

| Requirement | Spec |
|-------------|------|
| Microphone | USB (Blue Yeti, AT2020 recommended) |
| Format | WAV, 22050Hz, Mono, 16-bit |
| Duration | 1.5-2 hours total |
| Environment | Quiet room, pop filter |
| Software | Audacity (free) |

### Recording Script Contents
- **Section 1:** Basic greetings (15 min)
- **Section 2:** Common commands (20 min)
- **Section 3:** Conversational phrases (25 min)
- **Section 4:** Questions & responses (20 min)
- **Section 5:** Emotional range (15 min)
- **Section 6:** Alice identity phrases (20 min)

### Training Options

**Local (GPU recommended):**
```bash
pip install piper-tts
python train_piper.py --dataset ./voice_training/dataset.json
```

**Docker:**
```bash
docker run --gpus all -it -v $(pwd):/workspace \
  ghcr.io/rhasspy/piper:latest \
  python /scripts/train.py --dataset /workspace/voice_training/dataset.json
```

**Cloud (easier):**
- RunPod, Lambda Labs, or Google Colab Pro

📖 **Full Guide:** [Piper Training Documentation](https://github.com/rhasspy/piper/blob/master/docs/training.md)

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
