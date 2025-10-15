# VS Code Launch Quick Reference

This is a quick reference guide for using the VS Code launch configurations with Llama 3.

## 🚀 Quick Start

1. **Open in VS Code**: `code .`
2. **Press F5** (or click the Run icon ▶️ in the left sidebar)
3. **Select a configuration** from the dropdown at the top of the debug panel
4. **Watch it run!** 

## 📋 Available Configurations

| Configuration | Description | Use Case |
|--------------|-------------|----------|
| **Story Generator** | Generates creative stories | Quick content generation, testing model creativity |
| **Interactive Chatbot** | Multi-turn conversation | Building chat apps, testing conversation flow |
| **Chat Completion Example** | Official examples | Learning best practices, testing chat patterns |
| **Text Completion Example** | Text generation | Understanding base models, prompt engineering |
| **Hemp Seed Web App** | Flask web application | Building web services, customer-facing apps |

## 🎯 Common Tasks

### Change Story Topic
Edit `.vscode/launch.json`, find the Story Generator configuration, and change:
```json
"--topic",
"a brave knight"  // Change this to your topic
```

### Change Model Path
If your model is in a different location, update all configurations:
```json
"--ckpt_dir",
"YOUR_MODEL_PATH/",  // Change this
"--tokenizer_path",
"YOUR_MODEL_PATH/tokenizer.model"  // And this
```

### Change Web App Port
For Hemp Seed Web App, change:
```json
"--port",
"5000"  // Change to your preferred port
```

## 🐛 Debugging Features

### Setting Breakpoints
- Click in the left margin (gutter) next to line numbers
- Red dots appear where breakpoints are set
- Program pauses when it hits a breakpoint

### Debug Controls
- **Continue** (F5) - Resume execution
- **Step Over** (F10) - Execute current line, skip into functions
- **Step Into** (F11) - Enter into function calls
- **Step Out** (Shift+F11) - Exit current function
- **Restart** (Ctrl+Shift+F5) - Restart the program
- **Stop** (Shift+F5) - Stop debugging

### Debug Panel
- **Variables** - See all variables and their values
- **Watch** - Monitor specific expressions
- **Call Stack** - See the sequence of function calls
- **Debug Console** - Execute Python expressions

## ⚙️ Configuration Details

### Using torchrun vs Direct Python

**Apps that use torchrun:**
- Story Generator
- Interactive Chatbot  
- Chat Completion Example
- Text Completion Example

These use `"module": "torch.distributed.run"` in the launch configuration.

**Apps that use Python directly:**
- Hemp Seed Web App (Flask)

These use `"program": "${workspaceFolder}/hemp_seed_app.py"`.

### Why "justMyCode": false?

This setting allows you to step into library code (like the llama module) during debugging. Useful for understanding how things work under the hood.

### Why "console": "integratedTerminal"?

This ensures interactive input/output works properly, especially important for:
- Interactive Chatbot (you need to type responses)
- Hemp Seed Web App (shows server output)

## 🔧 Customization Examples

### Add a New Configuration

Copy an existing configuration in `.vscode/launch.json` and modify:

```json
{
    "name": "My Custom App",
    "type": "debugpy",
    "request": "launch",
    "module": "torch.distributed.run",
    "args": [
        "--nproc_per_node",
        "1",
        "my_custom_app.py",
        "--ckpt_dir",
        "Meta-Llama-3-8B-Instruct/",
        "--tokenizer_path",
        "Meta-Llama-3-8B-Instruct/tokenizer.model",
        "--my_arg",
        "my_value"
    ],
    "console": "integratedTerminal",
    "justMyCode": false,
    "cwd": "${workspaceFolder}"
}
```

### Multiple Story Topics

Create multiple configurations with different topics:

```json
{
    "name": "Story: Space Adventure",
    "type": "debugpy",
    "request": "launch",
    "module": "torch.distributed.run",
    "args": [
        "--nproc_per_node", "1",
        "my_first_app.py",
        "--ckpt_dir", "Meta-Llama-3-8B-Instruct/",
        "--tokenizer_path", "Meta-Llama-3-8B-Instruct/tokenizer.model",
        "--topic", "an astronaut exploring Mars"
    ],
    "console": "integratedTerminal",
    "justMyCode": false,
    "cwd": "${workspaceFolder}"
}
```

## 💡 Tips & Tricks

### Tip 1: Use Keyboard Shortcuts
- `F5` - Start/Continue debugging
- `F9` - Toggle breakpoint on current line
- `F10` - Step over
- `F11` - Step into

### Tip 2: Debug Console is Python REPL
While paused at a breakpoint, use the Debug Console to:
- Check variable values: `print(generator)`
- Test expressions: `len(conversation)`
- Call functions: `results[0]['generation']['content']`

### Tip 3: Conditional Breakpoints
Right-click a breakpoint → Edit Breakpoint → Add condition:
- `i == 5` - Break only when i equals 5
- `len(text) > 100` - Break when text is long

### Tip 4: Log Points
Right-click in gutter → Add Logpoint
- Message: `"Processing item {i}: {item}"`
- Logs without stopping execution

### Tip 5: Watch Expressions
Add expressions to Watch panel:
- `generator.model.params`
- `len(conversation)`
- `results[0]['generation']`

## 🆘 Troubleshooting

### "No module named 'torch'"
```bash
pip install -e .
```

### "debugpy not found"
```bash
pip install debugpy
```

### "Model directory not found"
Update the `--ckpt_dir` path in `.vscode/launch.json` to match your model location.

### Interactive Chatbot not accepting input
Make sure `"console": "integratedTerminal"` is set in the configuration.

### Hemp Seed Web App can't access
- Check the terminal for the URL (usually http://127.0.0.1:5000)
- Make sure port 5000 isn't already in use
- Try changing to a different port in the configuration

## 📚 Additional Resources

- [VS Code Python Debugging](https://code.visualstudio.com/docs/python/debugging)
- [LAUNCH.md](../LAUNCH.md) - All launch methods
- [TUTORIAL.md](../TUTORIAL.md) - Full Llama 3 tutorial
- [GETTING_STARTED.md](../GETTING_STARTED.md) - Getting started guide

---

**Happy Debugging! 🐛➡️✨**
