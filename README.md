# EAAP Gen AI Image Generator

A modern, user-friendly web application for generating AI-powered images using OpenAI's DALL-E 3 model. Built with Flask, featuring user authentication and a responsive interface.

## 🌟 Features

### Core Functionality
- **AI Image Generation**: Create stunning images from text descriptions using OpenAI's DALL-E 3
- **User Authentication**: Secure registration and login system
- **Responsive Design**: Clean, modern UI that works on all devices
- **Real-time Generation**: Asynchronous image generation with loading indicators
- **Session Management**: Persistent user sessions with Flask-Login

### Technical Highlights
- **High-Quality Images**: Generates 1024x1024 resolution images
- **Error Handling**: Comprehensive error handling for API failures and user input
- **Flash Messages**: User-friendly feedback for actions and errors
- **AJAX Integration**: Seamless form submission without page reloads

## 🚀 Quick Start

### Prerequisites
- Python 3.11 or higher
- OpenAI API key (get one at [OpenAI Platform](https://platform.openai.com/api-keys))

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd eaap-gen-ai-image-generator
   ```

2. **Set up Python environment**
   ```bash
   # Using uv (recommended - faster and more reliable)
   uv sync

   # Or using pip
   python -m venv myenv
   source myenv/bin/activate  # On Windows: myenv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure environment**
   ```bash
   # Set your OpenAI API key
   export OPENAI_API_KEY="your-api-key-here"
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

5. **Open your browser**
   Navigate to `http://127.0.0.1:5000/`

## 📋 Usage

### First Time Setup
1. **Register**: Create a new account with username and password
2. **Login**: Sign in with your credentials
3. **Generate Images**: Enter descriptive prompts to create AI images

### Image Generation
- Write detailed, creative prompts for best results
- Examples:
  - "A serene mountain landscape at sunset with vibrant colors"
  - "A futuristic cityscape with flying cars and neon lights"
  - "A cute cartoon character exploring a magical forest"

### Navigation
- **Home**: Main image generation interface
- **Login/Register**: User authentication pages
- **Logout**: Sign out of your account

## 🏗️ Project Structure

```
eaap-gen-ai-image-generator/
├── main.py                 # Flask application and routes
├── pyproject.toml          # Project configuration and dependencies
├── uv.lock                 # Dependency lock file
├── README.md              # This file
├── templates/             # HTML templates
│   ├── index.html         # Main image generator page
│   ├── login.html         # User login page
│   └── register.html      # User registration page
├── static/                # Static assets (CSS, JS, images)
└── services/              # Service modules (currently unused)
```

## 🔧 Configuration

### Environment Variables
- `OPENAI_API_KEY`: Your OpenAI API key (required)
- `FLASK_ENV`: Set to 'development' for debug mode

### Security Notes
- Change the `app.secret_key` in `main.py` to a secure random value
- The current implementation uses in-memory user storage
- For production, implement proper database storage

## 🛠️ Development

### Dependencies
- **Flask**: Web framework
- **Flask-Login**: User session management
- **OpenAI**: AI image generation API
- **Jinja2**: Template engine

### Key Components

#### User Authentication
```python
# User model with Flask-Login integration
class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password
```

#### Image Generation
```python
# OpenAI DALL-E 3 integration
response = client.images.generate(
    model="dall-e-3",
    prompt=user_prompt,
    size="1024x1024",
    quality="standard",
    n=1,
)
```

#### Route Protection
```python
@app.route("/")
@login_required  # Requires user authentication
def home():
    return render_template("index.html")
```

### Running Tests
```bash
# No tests implemented yet
# Add pytest for comprehensive testing
```

## 🚀 Deployment

### Local Development
```bash
python main.py
```

### Production Deployment
1. Set up a production WSGI server (Gunicorn, uWSGI)
2. Configure a proper database (PostgreSQL, MySQL)
3. Set secure environment variables
4. Use a reverse proxy (Nginx, Apache)

### Docker Deployment (Future Enhancement)
```dockerfile
# Dockerfile example
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "main.py"]
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guidelines
- Add docstrings to functions
- Write meaningful commit messages
- Test thoroughly before submitting PRs

## 📝 Future Enhancements

- [ ] **Database Integration**: Replace in-memory user storage
- [ ] **Image Gallery**: Save and display generated images
- [ ] **User Profiles**: Enhanced user management
- [ ] **API Rate Limiting**: Prevent API abuse
- [ ] **Batch Generation**: Generate multiple images at once
- [ ] **Image Editing**: Modify existing images
- [ ] **Social Features**: Share images, like/comment system
- [ ] **Admin Panel**: User and content management
- [ ] **API Endpoints**: REST API for external integrations
- [ ] **Mobile App**: Native mobile application

## 🐛 Known Issues

- User data is stored in memory (lost on restart)
- No password hashing (security risk)
- Limited error handling for OpenAI API failures
- No image storage or caching

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **OpenAI** for the DALL-E 3 model
- **Flask** community for the excellent web framework
- **Pallets Projects** for maintaining Flask ecosystem

## 📞 Support

For support, please open an issue on GitHub or contact the maintainers.

---

**Made with ❤️ using Flask and OpenAI's DALL-E 3**