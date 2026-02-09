# Browser Automation Integration

Integrate the screenshot analyzer with browser automation tools for automated testing and monitoring.

## Selenium WebDriver

```python
from selenium import webdriver
from src.screenshot_analyzer import ScreenshotAnalyzer

# Initialize
driver = webdriver.Chrome()
analyzer = ScreenshotAnalyzer()

# Navigate and capture
driver.get("https://example.com/login")
driver.save_screenshot("login.png")

# Analyze
result = analyzer.analyze_screenshot("login.png")
print(result)

driver.quit()
```

## Playwright (Recommended)

```python
from playwright.sync_api import sync_playwright
from src.screenshot_analyzer import ScreenshotAnalyzer

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    
    # Navigate
    page.goto("https://example.com/login")
    page.wait_for_load_state("networkidle")
    
    # Capture
    page.screenshot(path="login.png", full_page=True)
    browser.close()

# Analyze
analyzer = ScreenshotAnalyzer()
result = analyzer.analyze_screenshot("login.png")
```

## Batch Processing

```python
from playwright.sync_api import sync_playwright
from src.screenshot_analyzer import ScreenshotAnalyzer
import json

pages = [
    "https://example.com/login",
    "https://example.com/signup",
    "https://example.com/dashboard"
]

analyzer = ScreenshotAnalyzer()
results = {}

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    
    for url in pages:
        print(f"Analyzing: {url}")
        page.goto(url)
        page.wait_for_load_state("networkidle")
        
        screenshot_path = f"{url.split('/')[-1]}.png"
        page.screenshot(path=screenshot_path)
        
        results[url] = analyzer.analyze_screenshot(screenshot_path)
    
    browser.close()

# Save results
with open("batch_analysis.json", "w") as f:
    json.dump(results, f, indent=2)
```

## Base64 Integration (for APIs)

```python
from playwright.sync_api import sync_playwright
from src.screenshot_analyzer import ScreenshotAnalyzer
import base64

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://example.com/login")
    
    # Get screenshot as bytes
    screenshot_bytes = page.screenshot()
    browser.close()

# Convert to base64
screenshot_base64 = base64.b64encode(screenshot_bytes).decode('utf-8')

# Analyze
analyzer = ScreenshotAnalyzer()
result = analyzer.analyze_from_base64(screenshot_base64, mime_type="image/png")
```

## Installation

### Selenium
```bash
pip install selenium
# Download ChromeDriver from https://chromedriver.chromium.org/
```

### Playwright (Recommended)
```bash
pip install playwright
playwright install
```

## Tips

- Use `headless=True` for faster execution
- Wait for `networkidle` before capturing
- Use `full_page=True` for complete page capture
- Playwright is more modern and easier to set up
- Consider rate limiting for batch operations

## See Also

- [examples/example_browser_automation.py](../examples/example_browser_automation.py) - Full examples
- [Playwright Documentation](https://playwright.dev/python/)
- [Selenium Documentation](https://www.selenium.dev/documentation/)
