"""Alice OS Core - Orchestrates all modules"""
from .voice import VoiceInput
from .brain import Brain
from .home import SmartHome
from .habits import HabitTracker
from .finance import Finance
from .shopping import Shopping
from .context import ContextEngine

class AliceOS:
    def __init__(self):
        self.voice = VoiceInput()
        self.brain = Brain()
        self.home = SmartHome()
        self.habits = HabitTracker()
        self.finance = Finance()
        self.shopping = Shopping()
        self.context = ContextEngine()
    
    def run(self):
        """Main voice loop."""
        while True:
            # 1. Listen
            audio = self.voice.listen()
            # 2. Transcribe
            text = self.voice.transcribe(audio)
            # 3. Get context
            ctx = self.context.get_context()
            # 4. Think
            response = self.brain.think(text, ctx)
            # 5. Speak
            self.voice.speak(response)

if __name__ == "__main__":
    alice = AliceOS()
    alice.run()
