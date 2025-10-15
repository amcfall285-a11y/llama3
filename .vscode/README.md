# VS Code Launch Configurations for Llama 3

This directory contains VS Code launch configurations that allow you to easily run and debug Llama 3 applications directly from VS Code.

## 📖 Documentation

- **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)** - Comprehensive guide with tips, tricks, and examples
- **launch.json** - Launch configurations for all apps
- **This README** - Quick overview

## How to Use

1. **Open the project in VS Code**
   ```bash
   code .
   ```

2. **Select a configuration**
   - Press `F5` or click the Run icon in the sidebar
   - Select a configuration from the dropdown menu at the top

3. **Available Configurations:**
   - **Story Generator** - Generate creative stories on any topic
   - **Interactive Chatbot** - Chat interactively with the AI
   - **Chat Completion Example** - Run predefined conversation examples
   - **Text Completion Example** - Complete text prompts
   - **Hemp Seed Web App** - Launch the Flask web application

## Customizing Paths

The default configurations use `Meta-Llama-3-8B-Instruct/` as the model directory. If your model is in a different location, edit `.vscode/launch.json` and update:

```json
"--ckpt_dir",
"YOUR_MODEL_PATH/",
"--tokenizer_path",
"YOUR_MODEL_PATH/tokenizer.model"
```

## Requirements

- VS Code with the Python extension installed
- Python 3.8+
- Required packages: `pip install -e .`
- Llama 3 model downloaded

## Debugging

All configurations are set up for debugging:
- Set breakpoints by clicking in the left margin of code files
- Use the Debug Console to inspect variables
- Step through code with F10 (step over) and F11 (step into)

## Tips

- **Story Generator**: Change the `--topic` argument to generate stories about different topics
- **Interactive Chatbot**: Use the integrated terminal to type and chat
- **Hemp Seed Web App**: After launching, open your browser to `http://127.0.0.1:5000`

For more details, see [LAUNCH.md](../LAUNCH.md) in the root directory.
