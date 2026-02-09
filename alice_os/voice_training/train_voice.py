#!/usr/bin/env python3
"""
Alice OS - Complete Voice Training Pipeline
============================================

Usage:
    python train_voice.py --step setup       # Create directories & script
    python train_voice.py --step preprocess   # Process audio files
    python train_voice.py --step validate     # Check quality
    python train_voice.py --step prepare       # Create dataset
    python train_voice.py --step all          # Run full pipeline
    python train_voice.py --step train         # Train model (GPU required)

Requirements:
    - ffmpeg (for audio processing)
    - 2GB+ free disk space
    - GPU recommended for training
"""

import argparse
import subprocess
import sys
from pathlib import Path

# Configuration
TRAINING_DIR = Path(__file__).parent / "voice_training"
RECORDINGS_DIR = TRAINING_DIR / "recordings"
PROCESSED_DIR = TRAINING_DIR / "processed"
MODEL_DIR = TRAINING_DIR / "model"

def run_cmd(cmd, check=True):
    """Run a shell command."""
    print(f"🔧 Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)
    if check and result.returncode != 0:
        print(f"❌ Command failed: {' '.join(cmd)}")
        sys.exit(1)
    return result

def step_setup():
    """Create directory structure and recording script."""
    print("📁 Setting up training environment...")
    
    for dir_path in [TRAINING_DIR, RECORDINGS_DIR, PROCESSED_DIR, MODEL_DIR]:
        dir_path.mkdir(parents=True, exist_ok=True)
        print(f"  ✅ {dir_path}")
    
    # Generate recording script
    script_content = '''# Deanna's Voice Recording Script
# ==============================

# Section 1: Greetings
Hello, I am Alice.
Hello, how are you today?
Good morning!
Good afternoon!
Good evening!
Hi there!
Hey, what's up?
Nice to see you.
It's so good to hear from you.
How can I help you today?

# Section 2: Commands
Turn on the lights.
Turn off the lights.
Dim the lights to fifty percent.
Set the temperature to twenty-two degrees.
Lock the front door.
What's the weather like today?
Play some music.
Stop the music.
Add milk to my shopping list.
Remind me to call Mom at five.

# Section 3: Conversation
I'm here to help you with whatever you need.
I've noticed you've been working long hours today.
Would you like me to adjust the lighting for you?
Your favorite song is playing. Would you like to listen?
I've scheduled your appointments for tomorrow.
Don't forget to take a break soon.
I've ordered more coffee for you. It should arrive tomorrow.
You seem a bit tired. Maybe time for a rest?
I'm always here if you need me.
What would you like to do next?

# Section 4: Alice Identity
Hello, I am Alice. I am here to help.
I am your personal AI assistant.
I know your habits, your preferences, and your routines.
I am always learning to better help you.
I live in your home and your phone.
I control your lights, your music, and your schedule.
I keep track of your spending and your goals.
I am here to make your life easier.
Ask me anything. I'm ready to help.
I am Alice. What would you like to do?
'''
    
    with open(TRAINING_DIR / "script.txt", "w") as f:
        f.write(script_content)
    
    print(f"  ✅ Recording script: {TRAINING_DIR / 'script.txt'}")
    print("\n📝 Next steps:")
    print("1. Open script.txt and read each line")
    print("2. Record as WAV, 22050Hz, Mono, 16-bit")
    print("3. Name files: 001_hello.wav, 002_how_are_you.wav, etc.")
    print("4. Place in: recordings/")

def step_preprocess():
    """Convert all recordings to 22050Hz mono 16-bit WAV."""
    print("🎵 Preprocessing audio...")
    
    if not list(RECORDINGS_DIR.glob("*.wav")):
        print("⚠️ No WAV files found in recordings/")
        print(f"   Add recordings to: {RECORDINGS_DIR}")
        return
    
    for wav_file in RECORDINGS_DIR.glob("*.wav"):
        output_file = PROCESSED_DIR / wav_file.name
        run_cmd([
            "ffmpeg", "-y",
            "-i", str(wav_file),
            "-ar", "22050",
            "-ac", "1",
            "-c:a", "pcm_s16le",
            str(output_file)
        ])
        print(f"  ✅ {wav_file.name}")
    
    print(f"\n📁 Processed files: {PROCESSED_DIR}")

def step_validate():
    """Check recording quality and metadata."""
    print("🔍 Validating recordings...")
    
    import wave
    
    issues = []
    valid_count = 0
    
    for wav_file in RECORDINGS_DIR.glob("*.wav"):
        try:
            with wave.open(str(wav_file), 'r') as wf:
                frames = wf.getnframes()
                rate = wf.getframerate()
                duration = frames / float(rate)
                channels = wf.getnchannels()
                
                if rate != 22050:
                    issues.append(f"{wav_file.name}: Wrong sample rate ({rate}Hz)")
                if channels != 1:
                    issues.append(f"{wav_file.name}: Not mono ({channels} channels)")
                if duration < 1:
                    issues.append(f"{wav_file.name}: Too short ({duration:.2f}s)")
                else:
                    valid_count += 1
        except Exception as e:
            issues.append(f"{wav_file.name}: {str(e)}")
    
    if issues:
        print("⚠️ Issues found:")
        for issue in issues:
            print(f"  - {issue}")
    else:
        print(f"✅ All {valid_count} recordings look good!")
    
    return issues

def step_prepare():
    """Create dataset JSON for Piper training."""
    print("📊 Preparing dataset...")
    
    dataset = []
    script = {}
    
    # Load script mappings (simplified)
    script_file = TRAINING_DIR / "script.txt"
    if script_file.exists():
        lines = script_file.read_text().strip().split('\n')
        for i, line in enumerate(lines):
            if line and not line.startswith('#'):
                script[f"sample_{i+1}"] = line.strip()
    
    for i, wav_file in enumerate(sorted(RECORDINGS_DIR.glob("*.wav"))):
        sample_id = f"sample_{i+1}"
        dataset.append({
            "file": str(wav_file.relative_to(TRAINING_DIR)),
            "text": script.get(sample_id, sample_id),
            "id": sample_id
        })
    
    dataset_file = TRAINING_DIR / "dataset.json"
    with open(dataset_file, "w") as f:
        import json
        json.dump(dataset, f, indent=2)
    
    print(f"✅ Dataset saved: {dataset_file}")
    print(f"   Total samples: {len(dataset)}")

def step_train():
    """Train Piper TTS model (requires GPU)."""
    print("""
🚀 Training Piper TTS Model
============================

Option 1: Local Training (requires GPU)
---------------------------------------
pip install piper-tts
python train_piper.py --dataset ./voice_training/dataset.json

Option 2: Docker (Recommended)
------------------------------
docker run --gpus all -it -v $(pwd):/workspace \\
  ghcr.io/rhasspy/piper:latest \\
  python /scripts/train.py --dataset /workspace/voice_training/dataset.json

Option 3: Cloud Training
------------------------
- RunPod (GPU instances)
- Google Colab Pro
- Lambda Labs

📖 Full Guide: https://github.com/rhasspy/piper/blob/master/docs/training.md
""")

def main():
    parser = argparse.ArgumentParser(
        description="Alice OS - Deanna's Voice Training Pipeline"
    )
    parser.add_argument(
        "--step",
        choices=["setup", "preprocess", "validate", "prepare", "train", "all"],
        default="setup"
    )
    
    args = parser.parse_args()
    
    print("=" * 50)
    print("🎤 Alice OS - Voice Training Pipeline")
    print("=" * 50)
    
    if args.step == "setup":
        step_setup()
    elif args.step == "preprocess":
        step_preprocess()
    elif args.step == "validate":
        step_validate()
    elif args.step == "prepare":
        step_prepare()
        step_validate()
    elif args.step == "train":
        step_train()
    elif args.step == "all":
        step_setup()
        print()
        step_preprocess()
        print()
        step_validate()
        print()
        step_prepare()
        print()
        step_train()

if __name__ == "__main__":
    main()
