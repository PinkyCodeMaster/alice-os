"""Alice OS - Brain Module (Ollama LLM)"""
import ollama

class Brain:
    def __init__(self, model="llama3.2"):
        self.model = model
    
    def think(self, user_input, context=None):
        """Process user input and generate response."""
        # TODO: Implement context-aware thinking
        response = ollama.chat(model=self.model, messages=[
            {"role": "system", "content": "You are Alice, a helpful AI assistant."},
            {"role": "user", "content": user_input},
        ])
        return response["message"]["content"]
