# Llama 3 Examples and Tutorials

This directory contains examples and tutorials to help you get started with building applications using Llama 3.

## 🚀 Quick Links

- **[Quick Start Guide](QUICKSTART.md)** - Get running in 5 minutes
- **[Full Tutorial](TUTORIAL.md)** - Comprehensive step-by-step guide

## 📝 Example Applications

### 1. Story Generator (`my_first_app.py`)

A simple app that generates creative stories based on a topic.

**Features:**
- Single prompt story generation
- Customizable topic
- Creative temperature settings

**Run it:**
```bash
torchrun --nproc_per_node 1 my_first_app.py \
    --ckpt_dir Meta-Llama-3-8B-Instruct/ \
    --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model \
    --topic "a robot learning to paint"
```

### 2. Interactive Chatbot (`interactive_chatbot.py`)

A conversational AI that maintains context across multiple turns.

**Features:**
- Multi-turn conversations
- Conversation history
- Customizable system prompts
- Interactive command-line interface

**Run it:**
```bash
torchrun --nproc_per_node 1 interactive_chatbot.py \
    --ckpt_dir Meta-Llama-3-8B-Instruct/ \
    --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model
```

### 3. Chat Completion Examples (`example_chat_completion.py`)

Official example showing various chat completion scenarios.

**Run it:**
```bash
torchrun --nproc_per_node 1 example_chat_completion.py \
    --ckpt_dir Meta-Llama-3-8B-Instruct/ \
    --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model
```

### 4. Text Completion Examples (`example_text_completion.py`)

Official example for text completion with pre-trained models.

**Run it:**
```bash
torchrun --nproc_per_node 1 example_text_completion.py \
    --ckpt_dir Meta-Llama-3-8B/ \
    --tokenizer_path Meta-Llama-3-8B/tokenizer.model
```

## 🎯 Choose Your Path

### Beginner Path
1. Start with [QUICKSTART.md](QUICKSTART.md)
2. Run `my_first_app.py` to see basic generation
3. Try `interactive_chatbot.py` for multi-turn conversations
4. Read [TUTORIAL.md](TUTORIAL.md) for deeper understanding

### Advanced Path
1. Review [TUTORIAL.md](TUTORIAL.md) sections 4-7
2. Study the example applications
3. Modify examples for your use case
4. Build your custom application

## 📚 Learning Resources

### Step-by-Step Tutorials
- **QUICKSTART.md** - Fast track to your first app
- **TUTORIAL.md** - Complete guide with explanations
  - Environment setup
  - Understanding Llama 3 concepts
  - Building applications
  - Customization techniques
  - Deployment strategies

### Example Code
All examples include:
- Detailed comments
- Usage documentation
- Command-line interface
- Error handling

## 🛠️ Common Customizations

### Change Chatbot Personality
```python
system_prompt = {
    "role": "system",
    "content": "You are a helpful coding assistant. Provide clear, concise code examples."
}
```

### Adjust Response Style
```python
# More creative/random
results = generator.chat_completion(
    dialogs,
    temperature=0.9,  # Higher = more creative
    top_p=0.95,
)

# More focused/deterministic
results = generator.chat_completion(
    dialogs,
    temperature=0.3,  # Lower = more focused
    top_p=0.9,
)
```

### Control Response Length
```python
results = generator.chat_completion(
    dialogs,
    max_gen_len=128,  # Shorter responses
)
```

## 🔧 Troubleshooting

### Out of Memory
- Reduce `max_seq_len` (e.g., to 256)
- Reduce `max_batch_size` (to 1)
- Use smaller model variant

### Slow Performance
- Ensure GPU is being used: `torch.cuda.is_available()`
- Reduce `max_gen_len`
- Close other applications

### Import Errors
```bash
# Reinstall dependencies
pip install -e .
```

## 💡 Ideas for Your App

### Beginner Projects
- Personal journal assistant
- Story idea generator
- Simple Q&A bot
- Text summarizer

### Intermediate Projects
- Document analyzer
- Code review assistant
- Language learning tutor
- Recipe generator

### Advanced Projects
- Multi-agent system
- RAG (Retrieval-Augmented Generation) system
- Fine-tuned domain expert
- API service with web interface

## 🤝 Contributing

Found a bug or have an idea? See [CONTRIBUTING.md](CONTRIBUTING.md)

## 📖 Additional Resources

- [Llama Cookbook](https://github.com/meta-llama/llama-recipes) - More examples
- [Model Card](MODEL_CARD.md) - Technical details
- [Responsible Use Guide](https://ai.meta.com/static-resource/responsible-use-guide/) - Best practices

## ⚖️ License

See [LICENSE](LICENSE) and [USE_POLICY.md](USE_POLICY.md)

---

**Happy building!** 🎉 Start with the [Quick Start Guide](QUICKSTART.md) or dive into the [Full Tutorial](TUTORIAL.md).
