# Examples

Example scripts demonstrating various use cases.

## Files

### gemini_test.py
Basic test to verify Gemini API connectivity. Run this first to ensure your API key works.

```bash
python examples/gemini_test.py
```

### example_browser_automation.py
Comprehensive examples showing integration with:
- Selenium WebDriver
- Playwright
- Batch processing
- Base64 encoding

```bash
python examples/example_browser_automation.py
```

This displays code examples - copy and adapt them for your needs.

## Quick Examples

### Analyze a Screenshot
```python
from src.screenshot_analyzer import ScreenshotAnalyzer

analyzer = ScreenshotAnalyzer()
result = analyzer.analyze_screenshot("screenshot.png")
print(result)
```

### With Playwright
```python
from playwright.sync_api import sync_playwright
from src.screenshot_analyzer import ScreenshotAnalyzer

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://example.com")
    page.screenshot(path="page.png")
    browser.close()

analyzer = ScreenshotAnalyzer()
result = analyzer.analyze_screenshot("page.png")
```

## See Also

- [Browser Automation Guide](../docs/BROWSER_AUTOMATION.md)
- [Installation Guide](../docs/INSTALLATION.md)
