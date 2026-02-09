# Tab Analyzer Extension - Installation Guide

## Prerequisites

- Google Chrome or any Chromium-based browser (Edge, Brave, etc.)
- Gemini API Key from [Google AI Studio](https://aistudio.google.com/app/apikey)

## Installation Steps

### 1. Load the Extension

1. Open Chrome and navigate to: `chrome://extensions/`
2. Enable **Developer mode** (toggle in top-right corner)
3. Click **Load unpacked**
4. Select the `extension` folder from this repository
5. The Tab Analyzer extension should now appear in your extensions list

### 2. Pin the Extension (Optional but Recommended)

1. Click the puzzle piece icon in Chrome toolbar
2. Find "Tab Analyzer" in the list
3. Click the pin icon to keep it visible

### 3. Configure API Key

1. Click the Tab Analyzer extension icon
2. Enter your Gemini API Key in the input field
3. Click **Save**
4. The key is stored locally and securely in your browser

**Get your API key:** [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)

## Usage

1. Navigate to any webpage you want to analyze
2. Click the Tab Analyzer extension icon
3. Click **Analyze This Tab**
4. Wait a few seconds for the analysis
5. View the extracted data in the popup
6. Click **Copy JSON** to copy the raw data

## What Gets Analyzed

The extension extracts:
- ✓ Page title and main heading
- ✓ Form fields (labels, types, required status)
- ✓ Buttons and their purposes
- ✓ Navigation links
- ✓ Error/warning messages
- ✓ Page type classification
- ✓ Page description

## Troubleshooting

### Extension Not Loading

**Error:** "Manifest file is missing or unreadable"
- Make sure you selected the `extension` folder, not the parent folder
- Check that `manifest.json` exists in the folder

### API Key Issues

**Error:** "API request failed"
- Verify your API key is correct
- Check that your API key has Gemini API access enabled
- Try generating a new API key

### Screenshot Capture Fails

**Error:** "Cannot capture tab"
- Some pages (chrome://, chrome-extension://) cannot be captured
- Try on a regular webpage (http:// or https://)
- Refresh the page and try again

### No Results Showing

- Check browser console for errors (F12 → Console tab)
- Verify you have internet connection
- Try analyzing a simpler page first

## Permissions Explained

The extension requires these permissions:

- **activeTab**: To capture screenshots of the current tab
- **scripting**: To interact with the page content
- **host_permissions**: To work on all websites

Your data is never stored or sent anywhere except directly to Google's Gemini API.

## Updating the Extension

1. Make changes to the extension files
2. Go to `chrome://extensions/`
3. Click the refresh icon on the Tab Analyzer card
4. Changes will take effect immediately

## Uninstalling

1. Go to `chrome://extensions/`
2. Find Tab Analyzer
3. Click **Remove**
4. Your API key will be deleted from local storage

## Privacy & Security

- API key is stored locally in Chrome's storage (not sent anywhere)
- Screenshots are sent only to Google's Gemini API
- No data is stored on any server
- Extension works entirely client-side

## Support

For issues or questions:
- Check the troubleshooting section above
- Review the [Gemini API documentation](https://ai.google.dev/gemini-api/docs)
- Verify your API key at [Google AI Studio](https://aistudio.google.com/)
