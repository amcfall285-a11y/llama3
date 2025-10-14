# 🚀 Getting Started with Llama 3

Welcome! This guide will help you navigate all the resources available for building apps with Llama 3.

## 📖 Documentation Overview

We've created a comprehensive set of tutorials and guides to help you at every stage:

```
Your Journey:
┌─────────────────┐
│ New to Llama 3? │
└────────┬────────┘
         │
         ▼
┌─────────────────────┐      ┌──────────────────────┐
│  QUICKSTART.md      │ ───▶ │   TUTORIAL.md        │
│  (5 minute setup)   │      │   (Full guide)       │
└─────────────────────┘      └──────────┬───────────┘
         │                              │
         ▼                              ▼
┌─────────────────────┐      ┌──────────────────────┐
│  Run Example Apps   │      │   CHEATSHEET.md      │
│  - my_first_app.py  │      │   (Code reference)   │
│  - chatbot.py       │      └──────────────────────┘
└─────────────────────┘
         │
         ▼
┌─────────────────────┐
│  Build Your App!    │
└─────────────────────┘
```

## 🎯 Choose Your Path

### Path 1: Quick Start (5 minutes)
Perfect if you want to see results fast!

1. **[QUICKSTART.md](QUICKSTART.md)** - Installation and first run
2. Run `my_first_app.py` or `interactive_chatbot.py`
3. Start experimenting!

### Path 2: Learning Path (30 minutes)
Best for understanding how everything works:

1. **[TUTORIAL.md](TUTORIAL.md)** - Read sections 1-4 (Setup & Basics)
2. **[TUTORIAL.md](TUTORIAL.md)** - Follow section 5 (Build First App)
3. **[TUTORIAL.md](TUTORIAL.md)** - Try section 6 (Interactive Chatbot)
4. **[CHEATSHEET.md](CHEATSHEET.md)** - Keep for reference

### Path 3: Developer Path (10 minutes)
For experienced developers:

1. **[CHEATSHEET.md](CHEATSHEET.md)** - Quick code patterns
2. **[EXAMPLES.md](EXAMPLES.md)** - Overview of examples
3. Clone and modify example apps
4. Build your custom solution

## 📚 Document Guide

| Document | Purpose | Time | Best For |
|----------|---------|------|----------|
| **[FAQ.md](FAQ.md)** | Quick answers | 2 min | Common questions |
| **[QUICKSTART.md](QUICKSTART.md)** | Fast setup | 5 min | Getting running quickly |
| **[TUTORIAL.md](TUTORIAL.md)** | Complete guide | 30 min | Understanding concepts |
| **[EXAMPLES.md](EXAMPLES.md)** | Example overview | 10 min | Exploring possibilities |
| **[CHEATSHEET.md](CHEATSHEET.md)** | Code reference | 5 min | Quick lookup |

## 🔨 Example Applications

### my_first_app.py - Story Generator
**What it does:** Generates creative stories based on topics  
**Best for:** Understanding basic Llama 3 usage  
**Run time:** ~30 seconds

```bash
torchrun --nproc_per_node 1 my_first_app.py \
    --ckpt_dir Meta-Llama-3-8B-Instruct/ \
    --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model \
    --topic "your topic here"
```

### interactive_chatbot.py - Conversational AI
**What it does:** Multi-turn conversations with context  
**Best for:** Building interactive applications  
**Run time:** Ongoing (type 'quit' to exit)

```bash
torchrun --nproc_per_node 1 interactive_chatbot.py \
    --ckpt_dir Meta-Llama-3-8B-Instruct/ \
    --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model
```

### example_chat_completion.py - Official Examples
**What it does:** Demonstrates various chat patterns  
**Best for:** Learning official usage patterns

### example_text_completion.py - Text Generation
**What it does:** Shows text completion with base models  
**Best for:** Understanding pre-trained model usage

## 💡 What Can You Build?

### Beginner Projects
- ✍️ Personal writing assistant
- 📝 Note-taking companion
- 🎨 Story/poem generator
- ❓ Q&A bot

### Intermediate Projects
- 📄 Document summarizer
- 💻 Code explanation tool
- 🌍 Language tutor
- 📧 Email composer

### Advanced Projects
- 🤖 Multi-agent systems
- 🔍 RAG-based search
- 🎯 Domain-specific expert
- 🌐 Web API service

## 🛠️ Prerequisites

Before starting, ensure you have:

- ✅ Python 3.8 or higher
- ✅ CUDA GPU (recommended) or CPU
- ✅ 16GB+ RAM (for 8B model)
- ✅ Basic Python knowledge
- ✅ Command line familiarity

## 📦 Installation

```bash
# Clone repository
git clone https://github.com/meta-llama/llama3.git
cd llama3

# Install dependencies
pip install -e .

# Download model (requires registration)
./download.sh
```

For detailed installation steps, see [QUICKSTART.md](QUICKSTART.md).

## 🔍 Quick Reference

### Load Model
```python
from llama import Llama

generator = Llama.build(
    ckpt_dir="Meta-Llama-3-8B-Instruct/",
    tokenizer_path="Meta-Llama-3-8B-Instruct/tokenizer.model",
    max_seq_len=512,
    max_batch_size=1,
)
```

### Generate Response
```python
dialogs = [[{"role": "user", "content": "Your question here"}]]
results = generator.chat_completion(dialogs, max_gen_len=256)
print(results[0]['generation']['content'])
```

For more patterns, see [CHEATSHEET.md](CHEATSHEET.md).

## 🆘 Getting Help

### Common Issues
- **Out of Memory:** Reduce `max_seq_len` or use smaller model
- **Slow Performance:** Ensure GPU is being used
- **Import Errors:** Reinstall with `pip install -e .`

### Resources
- 📖 [Full Tutorial](TUTORIAL.md) - Detailed guide
- 🔧 [Troubleshooting](TUTORIAL.md#troubleshooting) - Common solutions
- 🐛 [GitHub Issues](https://github.com/meta-llama/llama3/issues) - Report bugs
- 📚 [Llama Cookbook](https://github.com/meta-llama/llama-recipes) - More examples

## 🎓 Learning Resources

### Official Documentation
- [README.md](README.md) - Repository overview
- [MODEL_CARD.md](MODEL_CARD.md) - Model details
- [USE_POLICY.md](USE_POLICY.md) - Usage guidelines

### External Resources
- [Llama Website](https://llama.meta.com/)
- [Hugging Face Models](https://huggingface.co/meta-llama)
- [Responsible Use Guide](https://ai.meta.com/static-resource/responsible-use-guide/)

## 🚀 Next Steps

1. **Start:** Pick a path above and begin!
2. **Experiment:** Modify the example apps
3. **Build:** Create your own application
4. **Share:** Contribute back to the community

## 📝 Quick Links

- [FAQ](FAQ.md) - Common questions answered
- [Quick Start](QUICKSTART.md) - 5-minute setup
- [Full Tutorial](TUTORIAL.md) - Complete guide
- [Examples](EXAMPLES.md) - Example apps
- [Cheatsheet](CHEATSHEET.md) - Code reference
- [Main README](README.md) - Repository home

---

**Ready to build?** Start with [QUICKSTART.md](QUICKSTART.md)! 🎉
