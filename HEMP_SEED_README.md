# The Hemp Seed - AI-Powered Web Application

## Overview

The Hemp Seed is a Flask-based web application that demonstrates the power of Llama 3 AI in a practical business context. This application provides an intelligent customer service assistant for a fictional hemp seed products store, showcasing how AI can be used to:

- Answer customer questions about products
- Provide nutritional and health information
- Suggest recipes and usage ideas
- Offer personalized recommendations
- Maintain natural conversation flow

The application features a beautiful, responsive web interface with real-time chat capabilities powered by Meta's Llama 3 language model.

## Features

- 🤖 **AI-Powered Chat Assistant** - Natural language conversation using Llama 3
- 🌿 **Hemp Product Expert** - Knowledgeable about hemp seeds, benefits, and products
- 💬 **Context-Aware Conversations** - Maintains conversation history for coherent dialogue
- 🎨 **Beautiful UI** - Modern, responsive design with gradient themes
- 📱 **Mobile-Friendly** - Works seamlessly on desktop and mobile devices
- 🔄 **Conversation Management** - Easy reset for new conversations
- 📊 **Product Catalog** - Six premium hemp products with detailed information
- 🍳 **Recipe Suggestions** - AI provides hemp seed recipe ideas

## What Customers Can Ask About

- 🌱 **Health Benefits** - Nutrition facts, omega-3/6, protein content
- 🛍️ **Products** - Available products, prices, recommendations
- 🍳 **Recipes** - Hemp seed smoothies, energy balls, pesto, granola
- 💡 **Usage Ideas** - How to incorporate hemp seeds into daily diet
- 📦 **Ordering** - Shipping information, store hours, contact details
- 💚 **General Hemp Info** - What are hemp seeds, how they're processed

## Installation

### Prerequisites

1. **Llama 3 Model Files** - Download the Llama 3 model checkpoint and tokenizer:
   ```bash
   # Run the download script from the main llama3 repository
   ./download.sh
   ```

2. **Python Dependencies** - Install required packages:
   ```bash
   pip install torch fairscale fire tiktoken blobfile
   pip install flask
   ```

### Directory Structure

Ensure your directory looks like this:
```
llama3/
├── hemp_seed_app.py           # Main Flask application
├── templates/
│   └── hemp_seed.html         # Web interface template
├── llama/                     # Llama 3 core files
├── Meta-Llama-3-8B-Instruct/  # Model checkpoint directory
└── tokenizer.model            # Tokenizer file
```

## Usage

### Starting the Application

Run the application using the `fire` CLI interface:

```bash
python hemp_seed_app.py \
    --ckpt_dir Meta-Llama-3-8B-Instruct/ \
    --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model
```

### Command-Line Arguments

- `--ckpt_dir` (required): Path to the model checkpoint directory
- `--tokenizer_path` (required): Path to the tokenizer model file
- `--max_seq_len` (optional): Maximum sequence length (default: 2048)
- `--host` (optional): Host address to bind the server (default: 127.0.0.1)
- `--port` (optional): Port number for the server (default: 5000)
- `--debug` (optional): Enable Flask debug mode (default: False)

### Example Commands

**Standard launch:**
```bash
python hemp_seed_app.py \
    --ckpt_dir Meta-Llama-3-8B-Instruct/ \
    --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model
```

**Custom port:**
```bash
python hemp_seed_app.py \
    --ckpt_dir Meta-Llama-3-8B-Instruct/ \
    --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model \
    --port 8080
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

Once the server starts, you'll see:
```
🚀 Loading Llama 3 model for The Hemp Seed app...
✅ Model loaded successfully!

🌿 Starting The Hemp Seed web application...
🌐 Open your browser and navigate to: http://127.0.0.1:5000
💬 Chat with our AI assistant about hemp seeds and products!

Press Ctrl+C to stop the server.
```

Open your web browser and navigate to `http://127.0.0.1:5000` (or the custom host/port you specified).

## Application Structure

### Backend (`hemp_seed_app.py`)

- **Flask Server** - Handles HTTP requests and serves the web interface
- **Llama 3 Integration** - Initializes and manages the AI model
- **Session Management** - Maintains conversation history per user
- **API Endpoints** - REST API for chat, reset, and product information

### Frontend (`templates/hemp_seed.html`)

- **Responsive Design** - Works on desktop and mobile devices
- **Real-time Chat UI** - Smooth message bubbles and animations
- **Product Sidebar** - Quick reference to products and information
- **Loading Indicators** - Visual feedback during AI processing

### Knowledge Base

The application includes comprehensive information about:
- 6 hemp seed products with prices and descriptions
- Health benefits and nutritional information
- Recipe ideas and usage suggestions
- Store location, hours, and contact information

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

### Model Loading Issues

**Problem:** "Model not found" or path errors  
**Solution:** Verify the checkpoint directory path and ensure model files are downloaded

### Flask Connection Issues

**Problem:** "Address already in use"  
**Solution:** Use a different port with `--port 5001` or stop other services using the port

### Memory Issues

**Problem:** Out of memory errors  
**Solution:** 
- Use GPU if available (automatic)
- Reduce `max_seq_len` parameter
- Close other memory-intensive applications

### Slow Response Times

**Problem:** AI responses are too slow  
**Solution:**
- Use a GPU for faster inference
- Reduce `max_seq_len` to 512 or 1024
- Use the 8B model instead of 70B if available

## Performance Tips

1. **Use GPU Acceleration** - Significantly faster inference with CUDA-enabled GPU
2. **Adjust Sequence Length** - Lower `max_seq_len` for faster responses
3. **Optimize Conversation History** - App keeps only last 10 exchanges to manage context
4. **Session Management** - Each user has independent conversation history
5. **Temperature Settings** - Adjust temperature (0.7) and top_p (0.9) for response quality vs. speed

## Production Deployment

⚠️ **Important:** This is a demonstration application. For production use:

1. **Security**
   - Use environment variables for sensitive data
   - Implement proper authentication
   - Enable HTTPS/SSL
   - Add rate limiting

2. **Scaling**
   - Use production WSGI server (Gunicorn, uWSGI)
   - Implement load balancing
   - Consider containerization (Docker)
   - Add caching layer

3. **Monitoring**
   - Add logging
   - Track performance metrics
   - Monitor model inference times
   - Set up error alerting

## Security Notes

- Default configuration runs on localhost only
- Don't expose to public internet without security measures
- Validate and sanitize all user inputs
- Implement rate limiting to prevent abuse
- Use environment variables for configuration
- Keep dependencies updated

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

- **Meta AI** - For the amazing Llama 3 language model
- **Flask** - Python web framework
- **The Hemp Seed Concept** - Demonstration of AI-powered business applications

---

**Ready to launch your hemp seed business with AI? 🌿✨**

Explore, customize, and build upon this application to create your own AI-powered customer experiences!
