"""
Deanna's Voice Training Script for Piper TTS
============================================

This script guides through recording Deanna's voice for Alice OS.

## Setup Requirements

1. **Recording Equipment:**
   - USB microphone (推荐: Blue Yeti, Audio-Technica AT2020)
   - Pop filter
   - Quiet room
   - Headphones for monitoring

2. **Software:**
   - Audacity (free) or Reaper (paid)
   - Export as: WAV, 22050Hz, Mono, 16-bit

## Piper TTS Training Process

Step 1: Record Dataset (1-2 hours)
Step 2: Audio Pre-processing
Step 3: Piper TTS Training
Step 4: Voice Model Testing
Step 5: Deploy to Alice OS

## Recording Script

See: training/script.txt for full recording script.
"""

import os
import wave
import json
from pathlib import Path

class VoiceTrainer:
    """Manages Deanna's voice training for Piper TTS."""
    
    def __init__(self, output_dir="./voice_model"):
        self.output_dir = Path(output_dir)
        self.recordings_dir = self.output_dir / "recordings"
        self.processed_dir = self.output_dir / "processed"
        self.model_dir = self.output_dir / "model"
        
        self.recordings_dir.mkdir(parents=True, exist_ok=True)
        self.processed_dir.mkdir(parents=True, exist_ok=True)
        self.model_dir.mkdir(parents=True, exist_ok=True)
    
    def generate_script(self):
        """Generate the recording script."""
        script = """
# Deanna's Voice Recording Script for Alice OS
# ===========================================

## Instructions
1. Read each line naturally at a comfortable pace
2. Take breaks between sections (2-3 min)
3. Stay hydrated but avoid water right before recording
4. Maintain consistent volume and tone
5. Record in a quiet environment

---

## Section 1: Basic Greetings (15 min)

1. Hello, I am Alice.
2. Hello, how are you today?
3. Good morning!
4. Good afternoon!
5. Good evening!
6. Hi there!
7. Hey, what's up?
8. Nice to see you.
9. It's so good to hear from you.
10. How can I help you today?

## Section 2: Common Commands (20 min)

1. Turn on the lights.
2. Turn off the lights.
3. Dim the lights to fifty percent.
4. Set the temperature to twenty-two degrees.
5. Lock the front door.
6. What's the weather like today?
7. Play some music.
8. Stop the music.
9. Add milk to my shopping list.
10. Remind me to call Mom at five.

## Section 3: Conversational Phrases (25 min)

1. I'm here to help you with whatever you need.
2. I've noticed you've been working long hours today.
3. Would you like me to adjust the lighting for you?
4. Your favorite song is playing. Would you like to listen?
5. I've scheduled your appointments for tomorrow.
6. Don't forget to take a break soon.
7. I've ordered more coffee for you. It should arrive tomorrow.
8. You seem a bit tired. Maybe time for a rest?
9. I'm always here if you need me.
10. What would you like to do next?

## Section 4: Questions & Responses (20 min)

1. What time is it?
2. What's on my schedule today?
3. How am I doing with my goals?
4. What's the weather forecast?
5. Did I spend much this week?
6. What's for dinner?
7. Am I on track with my habits?
8. What's happening in the world today?
9. How's the house doing?
10. Is anyone at the door?

## Section 5: Emotional Range (15 min)

1. That's wonderful news! I'm so happy for you.
2. Oh no, I'm sorry to hear that.
3. Wow, that's amazing!
4. I understand how you feel.
5. Take your time, I'm here.
6. You've got this! I believe in you.
7. That's perfectly okay, we all make mistakes.
8. I'm proud of what you've accomplished.
9. It's going to be alright.
10. I love helping you.

## Section 6: Alice-Specific (20 min)

1. Hello, I am Alice. I am here to help.
2. I am your personal AI assistant.
3. I know your habits, your preferences, and your routines.
4. I am always learning to better help you.
5. I live in your home and your phone.
6. I control your lights, your music, and your schedule.
7. I keep track of your spending and your goals.
8. I am here to make your life easier.
9. Ask me anything. I'm ready to help.
10. I am Alice. What would you like to do?

---

## Post-Recording Checklist

- [ ] All sections recorded
- [ ] Consistent volume throughout
- [ ] No background noise
- [ ] Each file is named correctly (e.g., "001_hello.wav")
- [ ] Total duration: 1.5-2 hours
"""
        
        with open(self.output_dir / "recording_script.txt", "w") as f:
            f.write(script)
        print(f"✅ Recording script saved to {self.output_dir / 'recording_script.txt'}")
    
    def preprocess_audio(self, input_file, output_file):
        """Process audio for Piper training."""
        import subprocess
        
        cmd = [
            "ffmpeg", "-y",
            "-i", input_file,
            "-ar", "22050",
            "-ac", "1",
            "-c:a", "pcm_s16le",
            output_file
        ]
        subprocess.run(cmd, check=True)
    
    def validate_recordings(self):
        """Check recording quality."""
        issues = []
        
        for wav_file in self.recordings_dir.glob("*.wav"):
            with wave.open(str(wav_file), 'r') as wf:
                frames = wf.getnframes()
                rate = wf.getframerate()
                duration = frames / float(rate)
                
                if duration < 1:  # Too short
                    issues.append(f"{wav_file.name}: Too short ({duration:.2f}s)")
        
        if issues:
            print("⚠️ Issues found:")
            for issue in issues:
                print(f"  - {issue}")
        else:
            print("✅ All recordings look good!")
        
        return issues
    
    def prepare_dataset(self):
        """Prepare dataset JSON for Piper training."""
        dataset = []
        
        for i, wav_file in enumerate(sorted(self.recordings_dir.glob("*.wav"))):
            # Get corresponding text (simplified - assumes numbered files)
            dataset.append({
                "file": str(wav_file.relative_to(self.output_dir)),
                "text": f"sample_{i+1}",  # Replace with actual text from script
                "audio": str(wav_file)
            })
        
        with open(self.output_dir / "dataset.json", "w") as f:
            json.dump(dataset, f, indent=2)
        
        print(f"✅ Dataset prepared: {len(dataset)} samples")
        return dataset
    
    def train(self):
        """Run Piper training (requires GPU and dataset)."""
        print("""
🚀 To train the voice model:

1. Install Piper:
   pip install piper-tts
   
2. Run training (requires GPU):
   python train_piper.py --dataset ./voice_model/dataset.json

3. Or use the official Piper Docker:
   docker run --gpus all -it ghcr.io/rhasspy/piper:latest

📖 Full guide: https://github.com/rhasspy/piper
        """)

if __name__ == "__main__":
    trainer = VoiceTrainer("./voice_training")
    trainer.generate_script()
    print("\n📝 Next steps:")
    print("1. Record audio using the script")
    print("2. Run: python voice_training.py --preprocess")
    print("3. Run: python voice_training.py --validate")
    print("4. Run: python voice_training.py --prepare")
    print("5. Run: python voice_trainer.py --train")
