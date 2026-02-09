# Quick Start Guide

Get started with the Browser Tab Screenshot Analyzer in 3 steps.

## Step 1: Verify Setup

Check that everything is configured:

```bash
# Check Python version (should be 3.11+)
python3 --version

# Check API key is set
echo $GEMINI_API_KEY

# Install dependencies
pip install -r requirements.txt
```

## Step 2: Test with a Screenshot

Take a screenshot of any browser tab and save it as `test.png`, then run:

```bash
python3 screenshot_analyzer.py test.png
```

You'll see:
- JSON output in the console
- Analysis saved to `test_analysis.json`

## Step 3: Integrate with Your Workflow

### Option A: Command Line

```bash
# Analyze any screenshot
python3 screenshot_analyzer.py login_page.png
python3 screenshot_analyzer.py signup_form.png
```

### Option B: Python Script

```python
from screenshot_analyzer import ScreenshotAnalyzer

analyzer = ScreenshotAnalyzer()
result = analyzer.analyze_screenshot("page.png")
print(result)
```

### Option C: Browser Automation

See `example_browser_automation.py` for integration examples with:
- Selenium WebDriver
- Playwright
- Batch processing
- Base64 encoding

Run examples:
```bash
python3 example_browser_automation.py
```

## What Gets Extracted?

The analyzer identifies:
- ✓ Page title and main heading
- ✓ Form fields (labels, types, required status)
- ✓ Buttons and their purposes
- ✓ Navigation links
- ✓ Error/warning messages
- ✓ Page type (login, signup, dashboard, etc.)

## Next Steps

- Read `INSTRUCTIONS.md` for detailed documentation
- Customize the schema in `screenshot_analyzer.py`
- Integrate with your browser automation tools
- Process multiple screenshots in batch

## Troubleshooting

**API Key Error?**
```bash
export GEMINI_API_KEY="your_key_here"
# Or add to ~/.zshrc for persistence
```

**Module Not Found?**
```bash
pip install -r requirements.txt
```

**Need Help?**
Check `INSTRUCTIONS.md` for comprehensive documentation.
