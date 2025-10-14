# The Hemp Seed Web App - Quick Start Guide

## 🌿 What You Got

Your **Hemp Seed** business now has a complete AI-powered web application! This app uses Llama 3 to provide intelligent customer service for your hemp seed products.

## ✨ Features at a Glance

### 1. AI Chat Assistant
- Answers questions about hemp seeds, benefits, and products
- Maintains conversation context
- Professional and friendly responses
- Powered by Llama 3 AI

### 2. Product Catalog
Six premium products included:
- Organic Raw Hemp Seeds ($12.99)
- Cold-Pressed Hemp Seed Oil ($18.99)
- Hemp Protein Powder ($24.99)
- Hemp Seed Butter ($15.99)
- Roasted Hemp Seeds ($9.99)
- Hemp Seed Flour ($13.99)

### 3. Knowledge Base
The AI knows about:
- Health benefits (Omega-3/6, protein, vitamins)
- Recipes (smoothies, energy balls, pesto, granola)
- Usage suggestions (salads, baking, toppings)
- Store information (hours, location, shipping)

### 4. Beautiful Interface
- Modern gradient design (green theme)
- Responsive layout (works on phone & desktop)
- Smooth animations
- Easy to navigate

## 🚀 How to Launch

### Step 1: Launch the App

**Easy Way (Using Launcher - Recommended):**
```bash
./launch_app.sh
# Choose option 5: The Hemp Seed Web App
# Press Enter for default port (5000)
```
*Note: The launcher automatically installs Flask if needed!*

**Direct Way:**
```bash
# First, ensure Flask is installed
pip install flask

# Then run the app
python hemp_seed_app.py \
    --ckpt_dir Meta-Llama-3-8B-Instruct/ \
    --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model
```

### Step 2: Open in Browser
Go to: **http://127.0.0.1:5000**

## 💬 Try These Example Questions

Once the app is running, try asking:

1. **"What are hemp seeds?"**
   - Get a comprehensive introduction

2. **"What products do you sell?"**
   - See the complete product catalog

3. **"What are the health benefits?"**
   - Learn about nutrition and wellness

4. **"Can you give me a recipe?"**
   - Get hemp seed recipe ideas

5. **"How much is the protein powder?"**
   - Ask about specific products

6. **"What are your store hours?"**
   - Get business information

## 🎨 What the Interface Looks Like

```
┌─────────────────────────────────────────────────────────────┐
│  🌿 The Hemp Seed - Premium Hemp Products                   │
├─────────────┬───────────────────────────────────────────────┤
│             │  💬 Chat with Our Hemp Expert         🔄 New  │
│ Sidebar:    ├───────────────────────────────────────────────┤
│             │                                                │
│ Why Hemp?   │  Chat Messages Area                           │
│ • Protein   │  (Conversations appear here)                  │
│ • Omega-3/6 │                                                │
│ • Heart     │                                                │
│             │                                                │
│ Products:   │                                                │
│ [Raw Seeds] │                                                │
│ [Hemp Oil]  │                                                │
│ [Protein]   │                                                │
│ [Butter]    │                                                │
│             ├───────────────────────────────────────────────┤
│ Contact:    │  [Type your message...]         [Send 🚀]    │
│ 📍 Location │                                                │
│ 🕒 Hours    │                                                │
│ 📧 Email    │                                                │
└─────────────┴───────────────────────────────────────────────┘
```

## 📁 File Structure

```
llama3/
├── hemp_seed_app.py           ← Main Flask app (AI logic)
├── templates/
│   └── hemp_seed.html         ← Web interface (UI)
├── HEMP_SEED_README.md        ← Full documentation
└── HEMP_SEED_QUICKSTART.md    ← This file
```

## 🔧 Customization Tips

### Change Products or Prices
Edit the `HEMP_SEED_INFO` variable in `hemp_seed_app.py`

### Modify Colors/Design
Edit the `<style>` section in `templates/hemp_seed.html`

### Adjust AI Responses
Modify the system prompt in the `/api/chat` route

### Change Port Number
```bash
python hemp_seed_app.py ... --port 8080
```

## 🆘 Troubleshooting

### "Flask not found"
**If using the launcher (./launch_app.sh):** Flask is automatically installed!

**If running directly:**
```bash
pip install flask
```

### "Port already in use"
```bash
python hemp_seed_app.py ... --port 5001
```

### "Model not found"
Make sure you've downloaded the model files:
```bash
./download.sh
```

### Slow responses
- Use GPU if available
- Lower max_seq_len (--max_seq_len 512)
- Close other applications

## 📖 Next Steps

1. **Read Full Docs**: Check `HEMP_SEED_README.md` for complete information
2. **Customize Content**: Update products, prices, and business info
3. **Test Thoroughly**: Try various customer questions
4. **Deploy**: Consider production deployment options
5. **Get Feedback**: Share with team members

## 🎯 What Makes This Special

- **AI-Powered**: Uses state-of-the-art Llama 3 model
- **Business-Specific**: Trained on hemp seed knowledge
- **Professional**: Production-ready code and design
- **Responsive**: Works on all devices
- **Easy to Use**: Simple setup and launch
- **Customizable**: Easy to modify content and styling
- **Well-Documented**: Complete guides included

## 💡 Use Cases

- Customer service on your website
- Product information kiosk
- Training tool for staff
- Marketing demo
- Educational resource
- Interactive catalog

## 🌟 Success Tips

1. Keep the conversation natural - the AI will follow your lead
2. Update product info regularly to stay current
3. Monitor conversations to improve responses
4. Add new recipes seasonally
5. Gather customer feedback
6. Share the app URL with customers

## 📞 Support

For issues or questions:
1. Check `HEMP_SEED_README.md` for detailed info
2. Review Llama 3 main documentation
3. Verify model and dependencies are installed
4. Check Flask documentation for web issues

---

**Your Hemp Seed business now has an AI assistant! 🌿✨**

Have fun exploring what your customers can learn about hemp seeds!
