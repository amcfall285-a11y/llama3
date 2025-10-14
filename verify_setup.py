#!/usr/bin/env python3
# Copyright (c) Meta Platforms, Inc. and affiliates.
# This software may be used and distributed in accordance with the terms of the Llama 3 Community License Agreement.

"""
Setup Verification Script

This script checks if your environment is properly configured to run Llama 3 apps.
Run this before attempting to launch apps to diagnose any issues.
"""

import sys
import os

def check_python_version():
    """Check if Python version is 3.8 or higher"""
    version = sys.version_info
    if version.major == 3 and version.minor >= 8:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} - OK")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor}.{version.micro} - Need 3.8 or higher")
        return False

def check_module(module_name, package_name=None):
    """Check if a Python module can be imported"""
    if package_name is None:
        package_name = module_name
    
    try:
        __import__(module_name)
        print(f"✅ {package_name} - Installed")
        return True
    except ImportError:
        print(f"❌ {package_name} - Not installed (run: pip install {package_name})")
        return False

def check_torch_details():
    """Check torch installation and CUDA availability"""
    try:
        import torch
        print(f"   PyTorch version: {torch.__version__}")
        print(f"   CUDA available: {torch.cuda.is_available()}")
        if torch.cuda.is_available():
            print(f"   CUDA version: {torch.version.cuda}")
            print(f"   GPU device: {torch.cuda.get_device_name(0)}")
        else:
            print("   Note: No GPU detected, will use CPU (slower)")
        return True
    except Exception as e:
        print(f"   Error checking torch details: {e}")
        return False

def check_model_files(ckpt_dir="Meta-Llama-3-8B-Instruct/"):
    """Check if model files exist"""
    if os.path.isdir(ckpt_dir):
        print(f"✅ Model directory found: {ckpt_dir}")
        
        tokenizer_path = os.path.join(ckpt_dir, "tokenizer.model")
        if os.path.isfile(tokenizer_path):
            print(f"✅ Tokenizer found: {tokenizer_path}")
            return True
        else:
            print(f"⚠️  Tokenizer not found: {tokenizer_path}")
            print("   Model directory exists but may be incomplete")
            return False
    else:
        print(f"❌ Model directory not found: {ckpt_dir}")
        print("   Download the model using: ./download.sh")
        return False

def main():
    print("🔍 Llama 3 Setup Verification")
    print("=" * 60)
    print()
    
    all_checks = []
    
    # Check Python version
    print("1. Checking Python version...")
    all_checks.append(check_python_version())
    print()
    
    # Check required packages
    print("2. Checking required packages...")
    all_checks.append(check_module("torch"))
    if all_checks[-1]:
        check_torch_details()
    all_checks.append(check_module("fairscale"))
    all_checks.append(check_module("fire"))
    all_checks.append(check_module("tiktoken"))
    all_checks.append(check_module("blobfile"))
    all_checks.append(check_module("flask"))
    print()
    
    # Check llama package
    print("3. Checking llama3 package...")
    llama_check = check_module("llama", "llama3 (run: pip install -e .)")
    all_checks.append(llama_check)
    print()
    
    # Check model files
    print("4. Checking model files...")
    model_check = check_model_files()
    print()
    
    # Summary
    print("=" * 60)
    if all(all_checks):
        print("✅ All dependency checks passed!")
        if model_check:
            print("✅ Model files found!")
            print()
            print("🚀 You're ready to launch! Run: ./launch_app.sh")
        else:
            print("⚠️  Dependencies OK, but model not found")
            print()
            print("📥 Next step: Download the model")
            print("   1. Visit https://llama.meta.com/llama-downloads/")
            print("   2. Register and get download URL")
            print("   3. Run: ./download.sh")
    else:
        print("❌ Some checks failed - see above for details")
        print()
        print("💡 To install dependencies: pip install -e .")
        print("💡 For detailed help: see LAUNCH.md")
    print("=" * 60)
    
    return 0 if all(all_checks) else 1

if __name__ == "__main__":
    sys.exit(main())
