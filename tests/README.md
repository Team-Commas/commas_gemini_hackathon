# Tests

Test directory for future test cases.

## Running Tests

Currently, use the example scripts to verify functionality:

```bash
# Test API connectivity
python examples/gemini_test.py

# Test screenshot analysis
python src/screenshot_analyzer.py path/to/screenshot.png
```

## Future Tests

Add unit tests here for:
- Schema validation
- API error handling
- Image format support
- Base64 encoding/decoding

## Test Framework

Consider using pytest:
```bash
pip install pytest
pytest tests/
```
