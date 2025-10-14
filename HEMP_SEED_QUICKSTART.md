# The Hemp Seed Web App - Quick Start Guide

Get your AI-powered hemp seed assistant running in minutes! 🌿

## ⚡ Quick Start (5 Minutes)

### Step 1: Download Model (if not already done)
```bash
./download.sh
```

### Step 2: Install Flask
```bash
pip install flask
```

### Step 3: Launch the App
```bash
python hemp_seed_app.py \
    --ckpt_dir Meta-Llama-3-8B-Instruct/ \
    --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model
```

### Step 4: Open Browser
Navigate to: `http://127.0.0.1:5000`

**That's it!** 🎉 Your hemp seed AI assistant is now running!

---

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

---

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

**On mobile:** Sidebar auto-hides for full-screen chat experience!

---

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

---

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

---

## 🆘 Troubleshooting

### "Flask not found"
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

## 📞 Support

For issues or questions:
1. Check `HEMP_SEED_README.md` for detailed info
2. Review Llama 3 main documentation
3. Verify model and dependencies are installed
4. Check Flask documentation for web issues

---

**Your Hemp Seed business now has an AI assistant! 🌿✨**

Have fun exploring what your customers can learn about hemp seeds!
