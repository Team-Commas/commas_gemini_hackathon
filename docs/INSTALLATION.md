# Browser Tab Screenshot Analyzer

Analyze browser tab screenshots and extract structured data using Gemini 3 Flash.

## Prerequisites

- **Python 3.11+** (required)
- **Gemini API Key** from [Google AI Studio](https://aistudio.google.com/app/apikey)

## Setup

### 1. Verify Python Version

```bash
python3 --version
# Should show Python 3.11 or higher
```

If you need Python 3.11, install it via Homebrew (macOS):
```bash
brew install python@3.11
```

### 2. Configure API Key

The API key is already configured in your `~/.zshrc` file:
```bash
export GEMINI_API_KEY="your_actual_api_key"
```

To verify it's set:
```bash
echo $GEMINI_API_KEY
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install google-genai pydantic Pillow
```

## Usage

### Command Line Interface

Analyze a screenshot from the command line:

```bash
python3 screenshot_analyzer.py path/to/screenshot.png
```

**Output:**
- Prints extracted JSON data to console
- Saves analysis to `screenshot_analysis.json`

**Supported formats:** PNG, JPEG, WebP, GIF

### Programmatic Usage

```python
from screenshot_analyzer import ScreenshotAnalyzer

# Initialize analyzer (uses GEMINI_API_KEY from environment)
analyzer = ScreenshotAnalyzer()

# Analyze from file path
result = analyzer.analyze_screenshot("screenshot.png")
print(result)

# Analyze from base64 string
result = analyzer.analyze_from_base64(base64_string, mime_type="image/png")
print(result)
```

### With Custom API Key

```python
analyzer = ScreenshotAnalyzer(api_key="your_api_key_here")
result = analyzer.analyze_screenshot("screenshot.png")
```

## Extracted Data Schema

The analyzer extracts the following information:

```json
{
  "page_title": "Login Page",
  "url": "https://example.com/login",
  "main_heading": "Sign In",
  "form_fields": [
    {
      "label": "Email",
      "field_type": "email",
      "value": null,
      "required": true
    }
  ],
  "buttons": [
    {
      "text": "Sign In",
      "button_type": "submit",
      "primary": true
    }
  ],
  "links": ["Forgot Password?", "Create Account"],
  "error_messages": [],
  "page_type": "login",
  "description": "User authentication page"
}
```

## Model Configuration

The analyzer uses **gemini-3-flash-preview** with optimized settings:

- **media_resolution**: `media_resolution_high` (1120 tokens) - Captures clear text and UI elements
- **response_mime_type**: `application/json` - Structured JSON output
- **thinking_level**: `low` - Faster processing for straightforward extraction
- **temperature**: 1.0 (default) - Balanced output

## Customizing the Schema

To extract different data, modify the Pydantic models in `screenshot_analyzer.py`:

```python
class BrowserTabSchema(BaseModel):
    """Add or modify fields here"""
    page_title: str
    custom_field: str = Field(description="Your custom field")
    # ... add more fields
```

The schema is automatically converted to JSON Schema and sent to Gemini.

## Browser Automation Integration

To capture screenshots programmatically, integrate with browser automation tools:

### Using Selenium

```python
from selenium import webdriver
from screenshot_analyzer import ScreenshotAnalyzer

# Capture screenshot
driver = webdriver.Chrome()
driver.get("https://example.com")
driver.save_screenshot("page.png")

# Analyze it
analyzer = ScreenshotAnalyzer()
result = analyzer.analyze_screenshot("page.png")
print(result)
```

### Using Playwright

```python
from playwright.sync_api import sync_playwright
from screenshot_analyzer import ScreenshotAnalyzer

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://example.com")
    page.screenshot(path="page.png")
    browser.close()

analyzer = ScreenshotAnalyzer()
result = analyzer.analyze_screenshot("page.png")
```

## Troubleshooting

### API Key Not Found

```
Error: API key not found
```

**Solution:** Ensure `GEMINI_API_KEY` is set in your environment:
```bash
export GEMINI_API_KEY="your_key"
# Or add to ~/.zshrc for persistence
```

### Module Not Found

```
ModuleNotFoundError: No module named 'google.genai'
```

**Solution:** Install dependencies:
```bash
pip install -r requirements.txt
```

### Image Format Not Supported

```
Error: Unsupported image format
```

**Solution:** Convert your image to PNG, JPEG, or WebP format.

### Low Quality Extraction

If the extracted data is incomplete:

1. Use higher resolution screenshots (1920x1080 or higher)
2. Enable v1alpha API for `media_resolution_high`:
   ```python
   result = analyzer.analyze_screenshot("screenshot.png", use_v1alpha=True)
   ```

## Examples

### Example 1: Login Page Analysis

```bash
python3 screenshot_analyzer.py login_page.png
```

Output:
```json
{
  "page_type": "login",
  "form_fields": [
    {"label": "Username", "field_type": "text", "required": true},
    {"label": "Password", "field_type": "password", "required": true}
  ],
  "buttons": [
    {"text": "Login", "button_type": "submit", "primary": true}
  ]
}
```

### Example 2: Form Validation

```bash
python3 screenshot_analyzer.py error_page.png
```

Output:
```json
{
  "error_messages": [
    "Invalid email format",
    "Password must be at least 8 characters"
  ]
}
```

## API Reference

### ScreenshotAnalyzer

**`__init__(api_key: Optional[str] = None)`**
- Initialize analyzer with optional API key
- If not provided, uses `GEMINI_API_KEY` environment variable

**`analyze_screenshot(image_path: str, use_v1alpha: bool = False) -> dict`**
- Analyze screenshot from file path
- `use_v1alpha`: Enable high-resolution processing (v1alpha API)
- Returns: Dictionary matching BrowserTabSchema

**`analyze_from_base64(base64_image: str, mime_type: str = "image/png") -> dict`**
- Analyze screenshot from base64 string
- Returns: Dictionary matching BrowserTabSchema

## Resources

- [Gemini 3 Documentation](https://ai.google.dev/gemini-api/docs/gemini-3)
- [Image Understanding Guide](https://ai.google.dev/gemini-api/docs/image-understanding)
- [Get API Key](https://aistudio.google.com/app/apikey)
