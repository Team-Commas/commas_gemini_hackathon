# Source Code

Core library for browser tab screenshot analysis.

## Files

### screenshot_analyzer.py
Main analysis engine with:
- `ScreenshotAnalyzer` class
- Pydantic schemas for structured data
- Support for file paths and base64 input
- Gemini 3 Flash integration

## Usage

### As a Module
```python
from src.screenshot_analyzer import ScreenshotAnalyzer

analyzer = ScreenshotAnalyzer()
result = analyzer.analyze_screenshot("screenshot.png")
```

### As a CLI Tool
```bash
python src/screenshot_analyzer.py screenshot.png
```

## Schema

The analyzer extracts data matching `BrowserTabSchema`:
- page_title
- url (optional)
- main_heading (optional)
- form_fields (array)
- buttons (array)
- links (array)
- error_messages (array)
- page_type
- description

## Customization

Modify the Pydantic models in `screenshot_analyzer.py` to extract different data:

```python
class BrowserTabSchema(BaseModel):
    # Add your custom fields
    custom_field: str = Field(description="Your field")
```

## API Configuration

The analyzer uses:
- Model: `gemini-3-flash-preview`
- Response format: JSON
- Thinking level: Low (faster processing)
- Media resolution: Standard (or high with v1alpha)
