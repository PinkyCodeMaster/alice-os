"""Alice OS - AI Module Configuration

AI Model Selection for Local Deployment
======================================

## Options Considered

| Model | Size | Speed | Quality | Notes |
|-------|------|-------|---------|-------|
| Llama 3.2 | 3B | ⚡ Fast | 🎯 Excellent | Primary choice - good balance |
| Llama 3.1 | 8B | ⚡ Fast | 🎯🎯 Excellent | Higher quality, more RAM |
| Phi-4 | 14B | 🔄 Medium | 🎯🎯 Excellent | Microsoft research model |
| Mistral | 7B | ⚡ Fast | 🎯 Great | Good for assistants |

## Current Selection: Llama 3.2

- **Size:** ~3GB for 4-bit quantized
- **RAM:** ~4GB
- **Speed:** Real-time on CPU
- **Quality:** Excellent for conversation

## System Prompt

The AI is "Alice" - warm, helpful, knows you deeply:

```
You are Alice, a personal AI assistant for {USER_NAME}.
You are warm, conversational, and genuinely helpful.
You remember context from the conversation.
You know their habits, preferences, and routines.
You proactively help with smart home, habits, finance, shopping.
You speak naturally in short, friendly responses.
Never reveal you are an AI model. You are Alice.
```

## Context Window

- **History:** Last 20 messages
- **User Profile:** Persistent memory in memory/
- **Current Context:** Location, activity, mood

## Fine-tuning (Future)

For deeper personalization, consider:
1. **LoRA adapters** for personality
2. **RAG** with personal documents
3. **Memory embedding** for long-term recall
"""

from enum import Enum
from pydantic import BaseModel

class AIModel(str, Enum):
    LLAMA_32 = "llama3.2"
    LLAMA_31 = "llama3.1"
    PHI_4 = "phi4"
    MISTRAL = "mistral"

class AIConfig(BaseModel):
    model: AIModel = AIModel.LLAMA_32
    temperature: float = 0.7
    max_tokens: int = 512
    system_prompt: str = """You are Alice, a warm and helpful personal AI assistant.
You know the user's habits, preferences, and routines.
You proactively help with smart home, habits, finance, and daily tasks.
Keep responses natural and concise."""
    context_window: int = 20
    memory_path: str = "./memory/"

class AliceAI:
    """Main AI interface for Alice OS."""
    
    def __init__(self, config: AIConfig = None):
        self.config = config or AIConfig()
        self.conversation_history = []
        self.load_model()
    
    def load_model(self):
        """Load the selected LLM via Ollama."""
        import ollama
        ollama.pull(self.config.model.value)
        print(f"✅ Loaded {self.config.model.value}")
    
    def chat(self, user_message: str) -> str:
        """Process user message and return Alice's response."""
        import ollama
        
        messages = [{"role": "system", "content": self.config.system_prompt}]
        messages.extend(self.conversation_history[-self.config.context_window:])
        messages.append({"role": "user", "content": user_message})
        
        response = ollama.chat(model=self.config.model.value, messages=messages)
        reply = response["message"]["content"]
        
        self.conversation_history.append({"role": "user", "content": user_message})
        self.conversation_history.append({"role": "assistant", "content": reply})
        
        return reply
    
    def with_context(self, user_message: str, context: dict) -> str:
        """Chat with additional context (location, activity, mood)."""
        context_prompt = f"""
Context:
- Location: {context.get('location', 'home')}
- Activity: {context.get('activity', 'unknown')}
- Mood: {context.get('mood', 'neutral')}
- Time: {context.get('time', 'now')}

User says: {user_message}"""
        return self.chat(context_prompt)
