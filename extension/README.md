# Tab Analyzer Chrome Extension

Analyze any browser tab and extract structured data using Gemini AI - no screenshots needed!

## Features

- 🔍 **One-Click Analysis** - Click the extension icon to analyze any webpage
- 📋 **Structured Data Extraction** - Automatically identifies forms, buttons, links, and more
- 🎯 **Smart Recognition** - Detects page types (login, signup, dashboard, etc.)
- 📊 **JSON Export** - Copy extracted data as JSON for further processing
- 🔒 **Privacy First** - API key stored locally, no data collection

## Quick Start

1. **Install the extension**
   ```bash
   # Open Chrome and go to: chrome://extensions/
   # Enable Developer mode
   # Click "Load unpacked" and select the extension folder
   ```

2. **Add your API key**
   - Click the extension icon
   - Enter your Gemini API key
   - Get one here: https://aistudio.google.com/app/apikey

3. **Analyze any page**
   - Navigate to any webpage
   - Click the extension icon
   - Click "Analyze This Tab"
   - View results instantly!

## What It Extracts

From any webpage:
- Page title and main heading
- Form fields (with types and required status)
- Buttons and their purposes
- Navigation links
- Error/warning messages
- Page type classification
- Descriptive summary

## Example Output

```json
{
  "page_title": "Login - Example App",
  "page_type": "login",
  "form_fields": [
    {
      "label": "Email",
      "field_type": "email",
      "required": true
    },
    {
      "label": "Password",
      "field_type": "password",
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
  "description": "User authentication page for Example App"
}
```

## Use Cases

- **QA Testing** - Quickly verify form fields and buttons
- **UI Documentation** - Auto-generate page element lists
- **Accessibility Audits** - Check form labels and structure
- **Competitive Analysis** - Analyze competitor interfaces
- **Automation Setup** - Identify elements for test scripts

## Technical Details

- **Model**: Gemini 3 Flash Preview
- **API**: Google Generative AI
- **Capture**: Chrome's native screenshot API
- **Processing**: Client-side only
- **Storage**: Local browser storage for API key

## Files

```
extension/
├── manifest.json       # Extension configuration
├── popup.html         # Extension popup UI
├── popup.js           # Main logic and API calls
├── icon16.png         # Toolbar icon
├── icon48.png         # Extension management icon
├── icon128.png        # Chrome Web Store icon
├── INSTALL.md         # Detailed installation guide
└── README.md          # This file
```

## Development

### Modify the Schema

Edit the `response_schema` in `popup.js` to extract different data:

```javascript
response_schema: {
  type: 'object',
  properties: {
    // Add your custom fields here
    custom_field: { type: 'string', description: 'Your field' }
  }
}
```

### Test Changes

1. Make your changes
2. Go to `chrome://extensions/`
3. Click refresh icon on Tab Analyzer
4. Test on a webpage

### Regenerate Icons

```bash
python3 create_icons.py
```

## Limitations

- Cannot capture Chrome internal pages (chrome://, chrome-extension://)
- Requires internet connection for API calls
- API rate limits apply (check Google AI Studio)
- Screenshot captures visible area only (no scrolling)

## Privacy

- API key stored locally in Chrome storage
- Screenshots sent only to Google Gemini API
- No data collection or tracking
- No external servers involved

## Troubleshooting

See [INSTALL.md](INSTALL.md) for detailed troubleshooting steps.

## License

MIT License - feel free to modify and distribute

## Credits

Built with:
- [Gemini API](https://ai.google.dev/gemini-api/docs)
- Chrome Extensions API
- Pillow (for icon generation)
