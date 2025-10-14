#!/usr/bin/env python3
"""
Llama 3 Launch Helper
A simple interactive helper to check your setup and launch apps easily.
"""

import os
import sys
import subprocess
from pathlib import Path


def print_header(text):
    """Print a formatted header."""
    print("\n" + "=" * 70)
    print(f"  {text}")
    print("=" * 70 + "\n")


def print_success(text):
    """Print success message."""
    print(f"✅ {text}")


def print_warning(text):
    """Print warning message."""
    print(f"⚠️  {text}")


def print_error(text):
    """Print error message."""
    print(f"❌ {text}")


def print_info(text):
    """Print info message."""
    print(f"ℹ️  {text}")


def check_python():
    """Check Python version."""
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print_success(f"Python {version.major}.{version.minor}.{version.micro} detected")
        return True
    else:
        print_error(f"Python {version.major}.{version.minor} is too old. Need Python 3.8+")
        return False


def check_dependencies():
    """Check if required dependencies are installed."""
    required = ['torch', 'fairscale', 'fire', 'tiktoken', 'flask']
    missing = []
    
    for package in required:
        try:
            __import__(package)
            print_success(f"{package} is installed")
        except ImportError:
            missing.append(package)
            print_warning(f"{package} is NOT installed")
    
    if missing:
        print_info("To install dependencies, run: pip install -e .")
        return False
    return True


def check_llama_package():
    """Check if llama package is installed."""
    try:
        import llama
        print_success("llama package is installed")
        return True
    except ImportError:
        print_warning("llama package is NOT installed")
        print_info("To install, run: pip install -e .")
        return False


def check_model():
    """Check if model files exist."""
    default_model_dir = Path("Meta-Llama-3-8B-Instruct")
    
    if default_model_dir.exists() and default_model_dir.is_dir():
        print_success(f"Model directory found: {default_model_dir}")
        tokenizer = default_model_dir / "tokenizer.model"
        if tokenizer.exists():
            print_success("Tokenizer file found")
            return True
        else:
            print_warning("Tokenizer file not found")
            return False
    else:
        print_warning(f"Model directory not found: {default_model_dir}")
        print_info("To download the model:")
        print_info("1. Visit https://llama.meta.com/llama-downloads/")
        print_info("2. Register and get download URL")
        print_info("3. Run: ./download.sh")
        return False


def check_launch_script():
    """Check if launch_app.sh exists and is executable."""
    launch_script = Path("launch_app.sh")
    
    if not launch_script.exists():
        print_error("launch_app.sh not found")
        return False
    
    if os.access(launch_script, os.X_OK):
        print_success("launch_app.sh is executable")
        return True
    else:
        print_warning("launch_app.sh is not executable")
        print_info("Run: chmod +x launch_app.sh")
        return False


def run_setup():
    """Run setup/installation."""
    print_header("Installing Dependencies")
    print_info("Running: pip install -e .")
    
    try:
        result = subprocess.run(
            ["pip", "install", "-e", "."],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print_success("Dependencies installed successfully!")
            return True
        else:
            print_error("Installation failed")
            print(result.stderr)
            return False
    except Exception as e:
        print_error(f"Installation failed: {e}")
        return False


def launch_app():
    """Launch the app using launch_app.sh."""
    print_header("Launching App")
    print_info("Starting launch_app.sh...")
    print()
    
    try:
        subprocess.run(["./launch_app.sh"])
    except KeyboardInterrupt:
        print("\n\nLaunch cancelled by user.")
    except Exception as e:
        print_error(f"Failed to launch: {e}")


def show_apps():
    """Show available applications."""
    print_header("Available Applications")
    
    apps = [
        ("my_first_app.py", "Story Generator", "Generate creative stories on any topic"),
        ("interactive_chatbot.py", "Interactive Chatbot", "Chat with AI in real-time"),
        ("example_chat_completion.py", "Chat Completion Example", "Run predefined conversation examples"),
        ("example_text_completion.py", "Text Completion Example", "Complete text prompts"),
        ("hemp_seed_app.py", "Hemp Seed Web App", "AI-powered business web application"),
    ]
    
    for i, (file, name, desc) in enumerate(apps, 1):
        exists = "✅" if Path(file).exists() else "❌"
        print(f"{i}. {exists} {name} ({file})")
        print(f"   {desc}")
        print()


def main():
    """Main function."""
    print_header("🚀 Llama 3 Launch Helper")
    
    print("This tool will help you check your setup and launch Llama 3 apps.\n")
    
    # Run all checks
    print_header("System Check")
    
    python_ok = check_python()
    deps_ok = check_dependencies()
    llama_ok = check_llama_package()
    model_ok = check_model()
    script_ok = check_launch_script()
    
    print()
    print_header("Summary")
    
    all_ok = python_ok and deps_ok and llama_ok and model_ok and script_ok
    
    if all_ok:
        print_success("All checks passed! You're ready to launch! 🎉")
        print()
        show_apps()
        
        while True:
            print()
            choice = input("Would you like to launch the app now? (y/n): ").lower().strip()
            if choice == 'y':
                launch_app()
                break
            elif choice == 'n':
                print_info("To launch later, run: ./launch_app.sh")
                break
            else:
                print_warning("Please enter 'y' or 'n'")
    else:
        print_warning("Some checks failed. Here's what you need to do:\n")
        
        if not python_ok:
            print("1. Install Python 3.8 or higher")
        
        if not deps_ok or not llama_ok:
            print("2. Install dependencies:")
            print("   Run: pip install -e .")
            print()
            choice = input("   Would you like me to install them now? (y/n): ").lower().strip()
            if choice == 'y':
                if run_setup():
                    print_success("Dependencies installed! Please run this script again.")
                    return
        
        if not model_ok:
            print("3. Download the Llama 3 model:")
            print("   a. Visit https://llama.meta.com/llama-downloads/")
            print("   b. Register and get download URL")
            print("   c. Run: ./download.sh")
        
        if not script_ok:
            print("4. Make launch script executable:")
            print("   Run: chmod +x launch_app.sh")
        
        print()
        print_info("For more help, see: LAUNCH_HELP.md")
        print_info("Or visit: https://github.com/meta-llama/llama3")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nAborted by user.")
        sys.exit(0)
    except Exception as e:
        print_error(f"An error occurred: {e}")
        sys.exit(1)
