# Contributing

This is a personal project, but you're welcome to fork and adapt it for your needs.

## Development Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up your API key: `export GEMINI_API_KEY="your_key"`
4. Run tests: `python examples/gemini_test.py`

## Project Structure

```
COMMAS/
├── src/              # Core library
├── extension/        # Chrome extension
├── examples/         # Example scripts
├── docs/            # Documentation
└── tests/           # Test cases
```

## Making Changes

1. Test your changes with example scripts
2. Update documentation if needed
3. Ensure code follows existing style
4. Add examples for new features

## Code Style

- Follow PEP 8 for Python code
- Use type hints where appropriate
- Add docstrings to functions and classes
- Keep functions focused and small

## Testing

Run the example scripts to verify functionality:
```bash
python examples/gemini_test.py
python src/screenshot_analyzer.py test.png
```

## Documentation

Update relevant docs when adding features:
- README.md for overview changes
- docs/INSTALLATION.md for setup changes
- docs/BROWSER_AUTOMATION.md for integration examples
- Add examples to examples/ directory

## Questions?

Open an issue or fork the project to experiment.
