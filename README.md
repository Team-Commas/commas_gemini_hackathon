# COMMAS - Browser Tab Screenshot Analyzer

AI-powered browser tab analysis using Google Gemini 3 Flash. Extract structured data from screenshots or live browser tabs without manual inspection.

## 🚀 Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Set your API key
export GEMINI_API_KEY="your_key_here"

# 3. Analyze a screenshot
python src/screenshot_analyzer.py screenshot.png
```

## 📦 What's Included

### Core Library (`src/`)
- **screenshot_analyzer.py** - Main analysis engine with Pydantic schemas

### Chrome Extension (`extension/`)
- Analyze any browser tab with one click
- No screenshots needed - works directly in Chrome
- See `docs/EXTENSION_QUICKSTART.md` for setup

### Examples (`examples/`)
- Basic Gemini API test
- Browser automation integration (Selenium, Playwright)
- Batch processing examples

### Documentation (`docs/`)
- Installation guide
- Quick start tutorial
- Extension setup
- Browser automation examples

## 🎯 Features

- **Structured Data Extraction** - Forms, buttons, links, error messages
- **Smart Page Classification** - Login, signup, dashboard, etc.
- **Multiple Input Methods** - File path, base64, or live browser capture
- **JSON Output** - Easy integration with automation tools
- **Chrome Extension** - One-click analysis without screenshots

## 📋 What Gets Extracted

```json
{
  "page_title": "Login Page",
  "page_type": "login",
  "form_fields": [
    {"label": "Email", "field_type": "email", "required": true},
    {"label": "Password", "field_type": "password", "required": true}
  ],
  "buttons": [
    {"text": "Sign In", "button_type": "submit", "primary": true}
  ],
  "links": ["Forgot Password?", "Create Account"],
  "error_messages": [],
  "description": "User authentication page"
}
```

## 🛠️ Use Cases

- **QA Testing** - Verify UI elements automatically
- **Documentation** - Generate page element inventories
- **Accessibility Audits** - Check form labels and structure
- **Test Automation** - Identify elements for Selenium/Playwright
- **Competitive Analysis** - Analyze competitor interfaces

## 📚 Documentation

- [Installation Guide](docs/INSTALLATION.md) - Detailed setup instructions
- [Quick Start](docs/QUICKSTART.md) - Get running in 3 steps
- [Extension Setup](docs/EXTENSION_QUICKSTART.md) - Chrome extension guide
- [Browser Automation](examples/example_browser_automation.py) - Integration examples

## 🔧 Requirements

- Python 3.11+
- Gemini API Key ([Get one here](https://aistudio.google.com/app/apikey))
- Chrome/Chromium (for extension only)

## 📁 Project Structure

```
COMMAS/
├── README.md                    # This file
├── requirements.txt             # Python dependencies
├── .env.example                 # Environment template
│
├── src/                         # Core library
│   └── screenshot_analyzer.py
│
├── extension/                   # Chrome extension
│   ├── manifest.json
│   ├── popup.html
│   ├── popup.js
│   └── *.png (icons)
│
├── examples/                    # Example scripts
│   ├── gemini_test.py
│   └── example_browser_automation.py
│
├── docs/                        # Documentation
│   ├── INSTALLATION.md
│   ├── QUICKSTART.md
│   └── EXTENSION_QUICKSTART.md
│
└── rcmFlow/                     # Separate project (unchanged)
```

## 🔐 Privacy

- API key stored locally only
- Screenshots sent only to Google Gemini API
- No data collection or external tracking
- Open source - audit the code yourself

## 📄 License

MIT License - Free to use and modify

## 🤝 Contributing

This is a personal project. Feel free to fork and adapt for your needs.

## 🔗 Resources

- [Gemini API Documentation](https://ai.google.dev/gemini-api/docs)
- [Get API Key](https://aistudio.google.com/app/apikey)
- [Gemini 3 Flash Guide](https://ai.google.dev/gemini-api/docs/gemini-3)
