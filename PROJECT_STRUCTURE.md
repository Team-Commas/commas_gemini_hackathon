# Project Structure

```
COMMAS/
│
├── README.md                           # Main project overview
├── CONTRIBUTING.md                     # Contribution guidelines
├── PROJECT_STRUCTURE.md                # This file
├── requirements.txt                    # Python dependencies
├── .env.example                        # Environment variables template
├── .gitignore                          # Git ignore rules
│
├── src/                                # Core library
│   ├── README.md                       # Source code documentation
│   └── screenshot_analyzer.py          # Main analysis engine
│
├── extension/                          # Chrome Extension
│   ├── README.md                       # Extension overview
│   ├── INSTALL.md                      # Installation guide
│   ├── manifest.json                   # Extension configuration
│   ├── popup.html                      # Extension UI
│   ├── popup.js                        # Extension logic
│   ├── create_icons.py                 # Icon generator script
│   └── icon*.png                       # Extension icons
│
├── examples/                           # Example scripts
│   ├── README.md                       # Examples overview
│   ├── gemini_test.py                  # Basic API test
│   └── example_browser_automation.py   # Integration examples
│
├── docs/                               # Documentation
│   ├── INSTALLATION.md                 # Detailed setup guide
│   ├── QUICKSTART.md                   # Quick start tutorial
│   ├── EXTENSION_QUICKSTART.md         # Extension setup guide
│   └── BROWSER_AUTOMATION.md           # Automation integration
│
├── tests/                              # Test directory
│   └── README.md                       # Testing guidelines
│
└── rcmFlow/                            # Separate project (unchanged)
    └── [rcmFlow project files]
```

## Directory Purposes

### `/src`
Core Python library for screenshot analysis. Import from here in your scripts.

### `/extension`
Chrome extension for one-click tab analysis. Load as unpacked extension in Chrome.

### `/examples`
Working example scripts demonstrating various use cases. Start here to learn.

### `/docs`
Comprehensive documentation for installation, usage, and integration.

### `/tests`
Test cases and testing utilities (to be expanded).

### `/rcmFlow`
Separate project - not part of COMMAS. Left unchanged.

## Quick Navigation

**Getting Started:**
- [README.md](README.md) - Start here
- [docs/QUICKSTART.md](docs/QUICKSTART.md) - 3-step setup

**Installation:**
- [docs/INSTALLATION.md](docs/INSTALLATION.md) - Detailed setup
- [requirements.txt](requirements.txt) - Dependencies

**Chrome Extension:**
- [extension/README.md](extension/README.md) - Extension overview
- [docs/EXTENSION_QUICKSTART.md](docs/EXTENSION_QUICKSTART.md) - Quick setup

**Examples:**
- [examples/gemini_test.py](examples/gemini_test.py) - Test API
- [examples/example_browser_automation.py](examples/example_browser_automation.py) - Automation

**Integration:**
- [docs/BROWSER_AUTOMATION.md](docs/BROWSER_AUTOMATION.md) - Selenium/Playwright

## File Count Summary

- Python files: 4
- Documentation: 10 markdown files
- Extension files: 7
- Configuration: 3 files
