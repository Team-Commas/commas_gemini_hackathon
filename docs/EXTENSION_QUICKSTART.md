# Chrome Extension Quick Start

Get the Tab Analyzer extension running in 3 minutes.

## Step 1: Load Extension (1 minute)

1. Open Chrome
2. Go to: `chrome://extensions/`
3. Toggle **Developer mode** ON (top-right)
4. Click **Load unpacked**
5. Select the `extension` folder from this project
6. ✓ Extension loaded!

## Step 2: Add API Key (1 minute)

1. Click the Tab Analyzer icon in Chrome toolbar
2. Enter your Gemini API key
3. Click **Save**

**Don't have a key?** Get one here: https://aistudio.google.com/app/apikey

## Step 3: Analyze a Tab (30 seconds)

1. Go to any webpage (try https://github.com/login)
2. Click the Tab Analyzer icon
3. Click **Analyze This Tab**
4. View the extracted data!

## What You'll See

The extension shows:
- Page title and type
- All form fields (email, password, etc.)
- Buttons and their purposes
- Navigation links
- Error messages (if any)
- Raw JSON you can copy

## Example

Try it on a login page:
```
Navigate to: https://github.com/login
Click extension → Analyze This Tab
Results:
  ✓ Page Type: login
  ✓ Form Fields: Username, Password (both required)
  ✓ Buttons: Sign in (primary)
  ✓ Links: Forgot password?, Create account
```

## Tips

- Pin the extension for quick access (click puzzle icon → pin)
- Use "Copy JSON" to export data
- Works on any webpage (except chrome:// pages)
- Analysis takes 2-5 seconds

## Troubleshooting

**Extension not showing?**
- Check you selected the `extension` folder (not parent folder)
- Look for the puzzle piece icon → Tab Analyzer

**API error?**
- Verify your API key is correct
- Get a new key from Google AI Studio

**Can't capture page?**
- Some pages (chrome://) can't be captured
- Try a regular website (http:// or https://)

## Next Steps

- Read `extension/INSTALL.md` for detailed docs
- Customize the schema in `popup.js`
- Use the JSON output in your automation scripts

That's it! You're now analyzing tabs directly without screenshots.
