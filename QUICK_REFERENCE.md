# Quick Reference

## Installation

```bash
pip install -r requirements.txt
export GEMINI_API_KEY="your_key_here"
```

## Basic Usage

### Analyze a Screenshot
```bash
python src/screenshot_analyzer.py screenshot.png
```

### Test API Connection
```bash
python examples/gemini_test.py
```

### View Examples
```bash
python examples/example_browser_automation.py
```

## Python API

```python
from src.screenshot_analyzer import ScreenshotAnalyzer

# Initialize
analyzer = ScreenshotAnalyzer()

# From file
result = analyzer.analyze_screenshot("screenshot.png")

# From base64
result = analyzer.analyze_from_base64(base64_string, mime_type="image/png")

# With custom API key
analyzer = ScreenshotAnalyzer(api_key="your_key")
```

## Chrome Extension

1. Open `chrome://extensions/`
2. Enable Developer mode
3. Click "Load unpacked"
4. Select `extension/` folder
5. Enter API key in extension popup
6. Click "Analyze This Tab" on any page

## Common Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Test Gemini API
python examples/gemini_test.py

# Analyze screenshot
python src/screenshot_analyzer.py image.png

# View automation examples
python examples/example_browser_automation.py

# Install browser automation (optional)
pip install playwright
playwright install
```

## Project Structure

```
COMMAS/
├── src/              # Core library
├── extension/        # Chrome extension
├── examples/         # Example scripts
├── docs/            # Documentation
└── tests/           # Test cases
```

## Documentation

- [README.md](README.md) - Project overview
- [docs/QUICKSTART.md](docs/QUICKSTART.md) - 3-step setup
- [docs/INSTALLATION.md](docs/INSTALLATION.md) - Detailed guide
- [docs/EXTENSION_QUICKSTART.md](docs/EXTENSION_QUICKSTART.md) - Extension setup
- [docs/BROWSER_AUTOMATION.md](docs/BROWSER_AUTOMATION.md) - Integration guide
- [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) - File organization

## Troubleshooting

**API Key Error:**
```bash
export GEMINI_API_KEY="your_key"
# Or add to ~/.zshrc for persistence
```

**Module Not Found:**
```bash
pip install -r requirements.txt
```

**Import Error:**
```python
# Use correct import path
from src.screenshot_analyzer import ScreenshotAnalyzer
```

## Get Help

- Check [docs/INSTALLATION.md](docs/INSTALLATION.md) for setup issues
- Run [examples/gemini_test.py](examples/gemini_test.py) to verify API
- See [examples/](examples/) for working code samples
- Review [CONTRIBUTING.md](CONTRIBUTING.md) for development info

## API Key

Get your free API key: https://aistudio.google.com/app/apikey
