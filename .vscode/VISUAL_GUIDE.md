# VS Code Launch Visual Guide

## 🎯 Simple 3-Step Process

```
┌─────────────────────────────────────────────────────────┐
│  Step 1: Open in VS Code                                │
│  $ code .                                                │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│  Step 2: Press F5 or Click Run Icon                     │
│  ▶️  Run and Debug (Ctrl+Shift+D)                        │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│  Step 3: Select Configuration                            │
│  🎨 Story Generator                                      │
│  💬 Interactive Chatbot                                  │
│  📋 Chat Completion Example                              │
│  ✍️  Text Completion Example                             │
│  🌿 Hemp Seed Web App                                    │
└─────────────────────────────────────────────────────────┘
```

## 🖥️ VS Code Interface

### Left Sidebar
```
┌─────┐
│ 📁  │ ← Explorer (file tree)
│ 🔍  │ ← Search
│ 🔀  │ ← Source Control (Git)
│ ▶️  │ ← Run and Debug ⭐ CLICK HERE
│ 🧩  │ ← Extensions
└─────┘
```

### Debug Panel (after clicking Run icon)
```
┌──────────────────────────────────────────────────┐
│ RUN AND DEBUG                                     │
├──────────────────────────────────────────────────┤
│                                                   │
│ [Story Generator (my_first_app.py)  ▼]  [▶️ F5] │
│                                                   │
│ VARIABLES                                         │
│ ▼ Locals                                         │
│   ▸ generator: Llama                             │
│   ▸ dialogs: list[1]                             │
│   ▸ results: list[1]                             │
│                                                   │
│ WATCH                                             │
│ + Add Expression                                  │
│                                                   │
│ CALL STACK                                        │
│ generate_story (my_first_app.py:39)              │
│                                                   │
│ BREAKPOINTS                                       │
│ ☑ my_first_app.py:55                             │
└──────────────────────────────────────────────────┘
```

## 🎬 Launch Configurations Overview

### Configuration 1: Story Generator
```
Name: Story Generator (my_first_app.py)
Type: Python with torchrun
Purpose: Generate creative stories
Default Topic: "a brave knight"

Example Output:
📝 Topic: a brave knight
Generating story...
📖 Generated Story:
============================================================
Once upon a time, in a kingdom far away, there lived a brave
knight named Sir Roland...
============================================================
```

### Configuration 2: Interactive Chatbot
```
Name: Interactive Chatbot
Type: Python with torchrun
Purpose: Multi-turn conversations
Interaction: Terminal input/output

Example Session:
👋 Hello! I'm your Llama 3 assistant. How can I help you today?

You: What is machine learning?
Assistant: Machine learning is a branch of artificial 
intelligence that enables computers to learn...

You: quit
👋 Goodbye! Have a great day!
```

### Configuration 3: Chat Completion Example
```
Name: Chat Completion Example
Type: Python with torchrun
Purpose: Demonstrate official chat patterns
Output: Multiple example conversations

Example:
User: what is the recipe of mayonnaise?
> Assistant: Mayonnaise is a thick, creamy condiment made from...

==================================

User: I am going to Paris, what should I see?
> Assistant: Paris, the capital of France...
```

### Configuration 4: Text Completion Example
```
Name: Text Completion Example
Type: Python with torchrun
Purpose: Text generation with base models
Output: Completed text prompts
```

### Configuration 5: Hemp Seed Web App
```
Name: Hemp Seed Web App
Type: Direct Python (Flask)
Purpose: AI-powered business web application
Access: http://127.0.0.1:5000

Features:
- Product information
- Recipe suggestions
- Health benefits Q&A
- Store information
```

## 🔧 Customization Workflow

### Change Story Topic
```
1. Open .vscode/launch.json
2. Find "Story Generator" configuration
3. Locate: "--topic", "a brave knight"
4. Change to: "--topic", "YOUR_TOPIC"
5. Save file
6. Press F5 to run with new topic
```

### Change Model Path
```
1. Open .vscode/launch.json
2. Find ALL occurrences of:
   "--ckpt_dir", "Meta-Llama-3-8B-Instruct/"
3. Replace with:
   "--ckpt_dir", "YOUR_MODEL_PATH/"
4. Find ALL occurrences of:
   "--tokenizer_path", "Meta-Llama-3-8B-Instruct/tokenizer.model"
5. Replace with:
   "--tokenizer_path", "YOUR_MODEL_PATH/tokenizer.model"
6. Save file
```

### Add New Configuration
```
1. Open .vscode/launch.json
2. Copy an existing configuration (between { and })
3. Paste after the last configuration
4. Add comma after previous configuration
5. Modify:
   - "name": "My New App"
   - Python file name
   - Arguments as needed
6. Save file
7. New configuration appears in dropdown
```

## 🐛 Debugging Workflow

### Setting Breakpoints
```
┌─────────────────────────────────────────┐
│ 1  #!/usr/bin/env python3              │
│ 2  from llama import Llama             │
│ 3                                       │
│ 4  def generate_story(...):            │
│ 5      print("Loading model...")        │
│ 🔴  generator = Llama.build(...)     ← Click here
│ 7      print("Model loaded!")           │
│ 8                                       │
│ 9      results = generator.chat(...)    │
│ 10     return results                   │
└─────────────────────────────────────────┘

When code reaches line 6, execution pauses.
You can inspect variables, step through code, etc.
```

### Debug Controls
```
┌─────────────────────────────────────────────┐
│ Continue (F5)      ▶️   Resume execution    │
│ Step Over (F10)    ⤵️   Execute this line   │
│ Step Into (F11)    ⬇️   Enter function      │
│ Step Out (⇧F11)    ⬆️   Exit function       │
│ Restart (⇧⌘F5)     🔄   Restart program     │
│ Stop (⇧F5)         ⏹️   Stop debugging      │
└─────────────────────────────────────────────┘
```

### Inspecting Variables
```
When paused at a breakpoint:

1. Variables Panel: See all local variables
   generator: <Llama object at 0x...>
   topic: "a brave knight"
   dialogs: [{"role": "user", "content": "..."}]

2. Hover over variable in code to see value
   
3. Debug Console: Type Python expressions
   >>> generator.model.params
   {'dim': 4096, 'n_layers': 32, ...}
   
   >>> len(dialogs)
   1
```

## 📊 Comparison: Launch Methods

### VS Code (F5) - Best for Development
```
✅ One keypress to launch
✅ Full debugging support
✅ Variable inspection
✅ Integrated terminal
✅ Breakpoints and stepping
✅ No command typing needed

Best For: Development, debugging, learning
```

### Launcher Script (./launch_app.sh) - Best for Guided Setup
```
✅ Interactive prompts
✅ Checks dependencies
✅ Helps configure paths
✅ User-friendly for beginners
❌ No debugging

Best For: First-time setup, non-developers
```

### Command Line (torchrun) - Best for Production
```
✅ Full control
✅ Scriptable
✅ Works in any environment
❌ Need to remember commands
❌ No debugging UI

Best For: Production, automation, CI/CD
```

## 🎓 Learning Path

### Beginner
```
1. Use VS Code launch configurations (this!)
2. Try Story Generator
3. Modify topic in launch.json
4. Run again
5. Experiment with other configs
```

### Intermediate
```
1. Set breakpoints in code
2. Step through execution
3. Inspect variables
4. Understand code flow
5. Create custom configuration
```

### Advanced
```
1. Debug library code (justMyCode: false)
2. Use conditional breakpoints
3. Watch complex expressions
4. Profile performance
5. Build custom apps with debugging
```

## 💡 Pro Tips

### Tip 1: Keyboard Maestro
```
F5      = Start/Continue
F9      = Toggle breakpoint
F10     = Step over
F11     = Step into
Shift+F11 = Step out
```

### Tip 2: Multiple Terminals
```
Terminal panel supports multiple terminals.
Useful for:
- Running app in one terminal
- Checking logs in another
- Running tests in a third
```

### Tip 3: Quick Configuration Switch
```
Click the configuration dropdown (top of debug panel)
Recent configurations appear first
No need to search through all configs
```

### Tip 4: Output Channels
```
Output panel (View > Output) shows:
- Python extension logs
- Debugger logs
- Build output
- Git operations
```

### Tip 5: Problems Panel
```
View > Problems (Ctrl+Shift+M)
Shows:
- Syntax errors
- Linting issues
- Runtime errors
Click to jump to problem location
```

## 🆘 Common Issues

### Issue: "Python extension not found"
```
Solution:
1. Open Extensions (Ctrl+Shift+X)
2. Search "Python"
3. Install "Python" by Microsoft
4. Reload VS Code
```

### Issue: "Module not found"
```
Solution:
Terminal (Ctrl+`) → Run:
$ pip install -e .
```

### Issue: "Debugpy not found"
```
Solution:
$ pip install debugpy
```

### Issue: "Model not found"
```
Solution:
1. Check model downloaded: ./download.sh
2. Update paths in .vscode/launch.json
3. Verify paths with: ls -la Meta-Llama-3-8B-Instruct/
```

### Issue: "Port already in use" (Hemp Seed App)
```
Solution:
1. Open .vscode/launch.json
2. Find Hemp Seed Web App config
3. Change: "--port", "5001"
4. Save and try again
```

## 📚 Additional Resources

- [VS Code Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial)
- [VS Code Debugging](https://code.visualstudio.com/docs/editor/debugging)
- [QUICK_REFERENCE.md](QUICK_REFERENCE.md) - Detailed guide
- [LAUNCH.md](../LAUNCH.md) - All launch methods
- [TUTORIAL.md](../TUTORIAL.md) - Llama 3 tutorial

---

**Happy Coding with VS Code! 🚀**
