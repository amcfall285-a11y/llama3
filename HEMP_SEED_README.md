# The Hemp Seed - AI-Powered Web Application

## Overview

**The Hemp Seed** is a Flask-based web application that uses Meta's Llama 3 AI model to provide an intelligent customer service assistant for a hemp seed products business. The application features an interactive chat interface where customers can ask questions about hemp seeds, their benefits, products, recipes, and more.

## Features

✅ **AI-Powered Chat Assistant** - Uses Llama 3 to answer customer questions intelligently  
✅ **Hemp Seed Knowledge Base** - Pre-loaded with product information, benefits, and recipes  
✅ **Conversation History** - Maintains context across multiple exchanges  
✅ **Modern Web Interface** - Beautiful, responsive design with gradient themes  
✅ **Product Catalog** - Display of available hemp seed products with prices  
✅ **Real-time Responses** - Instant AI-generated replies to customer inquiries  
✅ **Easy Reset** - Start new conversations with a single click  

## What Customers Can Ask About

- 🌱 **Health Benefits** - Nutrition facts, omega-3/6, protein content
- 🛍️ **Products** - Available products, prices, recommendations
- 🍳 **Recipes** - Hemp seed smoothies, energy balls, pesto, granola
- 💡 **Usage Ideas** - How to incorporate hemp seeds into daily diet
- 📦 **Ordering** - Shipping information, store hours, contact details
- 💚 **General Hemp Info** - What are hemp seeds, how they're processed

## Installation

### Prerequisites

- Python 3.8 or higher
- Llama 3 model files (downloaded via `./download.sh`)
- GPU recommended (can run on CPU but slower)

### Required Dependencies

The application requires Flask in addition to the standard Llama 3 dependencies:

```bash
# Install Flask
pip install flask

# Or add to requirements.txt
echo "flask>=2.3.0" >> requirements.txt
pip install -r requirements.txt
```

## Usage

### Starting the Server

Run the application using one of these methods:

#### Method 1: Direct Python Execution

```bash
python hemp_seed_app.py \
    --ckpt_dir Meta-Llama-3-8B-Instruct/ \
    --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model \
    --port 5000
```

#### Method 2: Using the Launcher Script

Update `launch_app.sh` to include The Hemp Seed app option (see instructions below).

### Command-Line Arguments

- `--ckpt_dir` (required): Path to model checkpoint directory
- `--tokenizer_path` (required): Path to tokenizer model file
- `--max_seq_len` (optional): Maximum sequence length (default: 2048)
- `--host` (optional): Host address (default: 127.0.0.1)
- `--port` (optional): Port number (default: 5000)
- `--debug` (optional): Enable Flask debug mode (default: False)
- `--open_browser` (optional): Automatically open browser (default: True)

### Example Commands

**Standard launch:**
```bash
python hemp_seed_app.py \
    --ckpt_dir Meta-Llama-3-8B-Instruct/ \
    --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model
```
*Browser opens automatically!*

**Custom port:**
```bash
python hemp_seed_app.py \
    --ckpt_dir Meta-Llama-3-8B-Instruct/ \
    --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model \
    --port 8080
```

**Disable auto-open browser:**
```bash
python hemp_seed_app.py \
    --ckpt_dir Meta-Llama-3-8B-Instruct/ \
    --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model \
    --open_browser=False
```

**Enable public access (use with caution):**
```bash
python hemp_seed_app.py \
    --ckpt_dir Meta-Llama-3-8B-Instruct/ \
    --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model \
    --host 0.0.0.0 \
    --port 5000
```

## Accessing the Application

1. Start the server using one of the methods above
2. **Browser opens automatically** - just wait a moment!
3. If browser doesn't open, manually navigate to: `http://127.0.0.1:5000` (or your custom host/port)
4. Start chatting with the Hemp Seed AI assistant!

## Application Structure

```
llama3/
├── hemp_seed_app.py          # Main Flask application
├── templates/
│   └── hemp_seed.html        # Web interface template
└── HEMP_SEED_README.md       # This file
```

## API Endpoints

The application provides several REST API endpoints:

### POST /api/chat
Send a message to the AI assistant.

**Request:**
```json
{
  "message": "What are the health benefits of hemp seeds?"
}
```

**Response:**
```json
{
  "response": "Hemp seeds are incredibly nutritious! They're rich in...",
  "conversation_length": 1
}
```

### POST /api/reset
Reset the conversation history.

**Response:**
```json
{
  "status": "Conversation reset successfully"
}
```

### GET /api/products
Get the list of available products.

**Response:**
```json
[
  {
    "name": "Organic Raw Hemp Seeds",
    "description": "Premium quality, unprocessed hemp seeds",
    "price": "$12.99",
    "size": "16 oz"
  },
  ...
]
```

## Customization

### Modifying Product Information

Edit the `HEMP_SEED_INFO` variable in `hemp_seed_app.py` to update:
- Product listings and prices
- Store information and hours
- Hemp seed benefits and uses
- Recipe suggestions

### Changing the AI Assistant's Personality

Modify the system prompt in the `/api/chat` route to adjust:
- Tone and style of responses
- Level of detail in answers
- Promotional vs. informational balance
- Conversation approach

### Updating the Visual Design

Edit `templates/hemp_seed.html` to customize:
- Color schemes and gradients
- Layout and spacing
- Typography and fonts
- Icons and emojis
- Product display cards

## Example Conversations

**Customer:** "What are hemp seeds?"  
**Assistant:** "Hemp seeds are the edible seeds of the hemp plant (Cannabis sativa). They're incredibly nutritious and don't contain THC..."

**Customer:** "Do you have hemp protein powder?"  
**Assistant:** "Yes! We have Hemp Protein Powder for $24.99 (1 lb). It contains 50% protein content and is perfect for smoothies..."

**Customer:** "Can you give me a recipe?"  
**Assistant:** "Here's a delicious Hemp Seed Smoothie recipe: Blend 2 tablespoons of hemp seeds with a banana, your favorite berries, and almond milk..."

## Troubleshooting

### Port Already in Use
If you get a "port already in use" error:
```bash
# Use a different port
python hemp_seed_app.py --ckpt_dir ... --tokenizer_path ... --port 5001
```

### Model Loading Errors
If the Llama model fails to load:
- Verify the `ckpt_dir` and `tokenizer_path` are correct
- Ensure you've downloaded the model files using `./download.sh`
- Check you have sufficient RAM/VRAM

### Slow Response Times
If responses are slow:
- Reduce `max_seq_len` to 512 or 1024
- Ensure GPU is available and being used
- Check system resources (RAM/VRAM usage)

### Session/Conversation Issues
If conversation history isn't working:
- Check that `app.secret_key` is set
- Ensure cookies are enabled in browser
- Try clearing browser cookies and restarting

## Performance Tips

1. **Use GPU**: Responses are much faster with GPU acceleration
2. **Adjust max_seq_len**: Lower values (512-1024) are faster but may limit context
3. **Limit History**: The app keeps last 20 messages (10 exchanges) to manage memory
4. **Close Other Apps**: Free up RAM/VRAM for better performance
5. **Use Production Server**: For deployment, use gunicorn or uwsgi instead of Flask dev server

## Production Deployment

For production use, consider:

1. **Use a production WSGI server:**
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 hemp_seed_app:app
```

2. **Set up HTTPS** with nginx or Apache as reverse proxy
3. **Enable logging** for monitoring and debugging
4. **Add rate limiting** to prevent abuse
5. **Implement authentication** if needed
6. **Use environment variables** for configuration
7. **Add database** for persistent conversation storage

## Security Notes

⚠️ **Important Security Considerations:**

- The app uses session-based conversation storage (temporary)
- `app.secret_key` is generated randomly on each start
- For production, set a persistent secret key via environment variable
- Don't expose debug mode in production (`debug=False`)
- Consider adding rate limiting for API endpoints
- Validate and sanitize user inputs
- Use HTTPS in production environments

## Future Enhancements

Ideas for extending The Hemp Seed app:

- 🛒 Shopping cart and checkout integration
- 📧 Email newsletter signup
- 📸 Product image gallery
- ⭐ Customer reviews and ratings
- 📱 Mobile app version
- 🌍 Multi-language support
- 📊 Analytics dashboard
- 💳 Payment processing integration
- 📦 Order tracking
- 🎁 Loyalty rewards program

## Support

For questions or issues with The Hemp Seed application:

1. Check this README for common solutions
2. Review the Llama 3 documentation in the main repository
3. Verify your model files and dependencies are correctly installed
4. Check Flask documentation for web server issues

## License

This application is built on Meta's Llama 3 and follows the Llama 3 Community License Agreement. See LICENSE file for details.

## Credits

- Built with Meta's Llama 3 AI model
- Web framework: Flask
- Frontend: HTML5, CSS3, JavaScript
- Created for The Hemp Seed business

---

**Enjoy your AI-powered hemp seed business! 🌿**
