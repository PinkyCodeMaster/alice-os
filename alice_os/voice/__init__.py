"""Alice OS - Voice Input Module (Whisper STT)"""
import whisper

class VoiceInput:
    def __init__(self):
        self.model = whisper.load_model("base")
    
    def listen(self):
        """Capture audio and convert to text."""
        # TODO: Implement audio capture
        pass
    
    def transcribe(self, audio_path):
        """Transcribe audio file to text."""
        result = self.model.transcribe(audio_path)
        return result["text"]
