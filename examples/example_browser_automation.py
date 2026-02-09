#!/usr/bin/env python3
"""
Example: Browser Automation with Screenshot Analysis
Demonstrates how to integrate screenshot_analyzer with Selenium or Playwright
"""

from screenshot_analyzer import ScreenshotAnalyzer
import json


def example_selenium():
    """Example using Selenium WebDriver"""
    print("=" * 80)
    print("EXAMPLE 1: Selenium Integration")
    print("=" * 80)
    print()
    print("Install Selenium first: pip install selenium")
    print()
    print("Code:")
    print("""
from selenium import webdriver
from screenshot_analyzer import ScreenshotAnalyzer

# Initialize browser
driver = webdriver.Chrome()

# Navigate to page
driver.get("https://example.com/login")

# Capture screenshot
driver.save_screenshot("login_page.png")

# Analyze screenshot
analyzer = ScreenshotAnalyzer()
result = analyzer.analyze_screenshot("login_page.png")

# Display results
print(json.dumps(result, indent=2))

# Clean up
driver.quit()
    """)


def example_playwright():
    """Example using Playwright"""
    print()
    print("=" * 80)
    print("EXAMPLE 2: Playwright Integration")
    print("=" * 80)
    print()
    print("Install Playwright first: pip install playwright")
    print("Then install browsers: playwright install")
    print()
    print("Code:")
    print("""
from playwright.sync_api import sync_playwright
from screenshot_analyzer import ScreenshotAnalyzer

with sync_playwright() as p:
    # Launch browser
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    
    # Navigate to page
    page.goto("https://example.com/login")
    
    # Wait for page to load
    page.wait_for_load_state("networkidle")
    
    # Capture screenshot
    page.screenshot(path="login_page.png", full_page=True)
    
    # Close browser
    browser.close()

# Analyze screenshot
analyzer = ScreenshotAnalyzer()
result = analyzer.analyze_screenshot("login_page.png")

# Display results
print(json.dumps(result, indent=2))
    """)


def example_batch_analysis():
    """Example: Analyze multiple pages"""
    print()
    print("=" * 80)
    print("EXAMPLE 3: Batch Analysis of Multiple Pages")
    print("=" * 80)
    print()
    print("Code:")
    print("""
from playwright.sync_api import sync_playwright
from screenshot_analyzer import ScreenshotAnalyzer
import json

# Pages to analyze
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
        
        # Navigate and capture
        page.goto(url)
        page.wait_for_load_state("networkidle")
        screenshot_path = f"{url.split('/')[-1]}.png"
        page.screenshot(path=screenshot_path)
        
        # Analyze
        result = analyzer.analyze_screenshot(screenshot_path)
        results[url] = result
    
    browser.close()

# Save all results
with open("batch_analysis.json", "w") as f:
    json.dump(results, f, indent=2)

print("✓ Batch analysis complete!")
    """)


def example_base64_integration():
    """Example using base64 encoding (useful for web APIs)"""
    print()
    print("=" * 80)
    print("EXAMPLE 4: Base64 Integration (for Web APIs)")
    print("=" * 80)
    print()
    print("Code:")
    print("""
from playwright.sync_api import sync_playwright
from screenshot_analyzer import ScreenshotAnalyzer
import base64

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://example.com/login")
    
    # Capture screenshot as bytes
    screenshot_bytes = page.screenshot()
    browser.close()

# Convert to base64
screenshot_base64 = base64.b64encode(screenshot_bytes).decode('utf-8')

# Analyze from base64
analyzer = ScreenshotAnalyzer()
result = analyzer.analyze_from_base64(screenshot_base64, mime_type="image/png")

print(json.dumps(result, indent=2))
    """)


def main():
    """Display all examples"""
    print()
    print("╔" + "=" * 78 + "╗")
    print("║" + " " * 20 + "BROWSER AUTOMATION EXAMPLES" + " " * 31 + "║")
    print("╚" + "=" * 78 + "╝")
    print()
    
    example_selenium()
    example_playwright()
    example_batch_analysis()
    example_base64_integration()
    
    print()
    print("=" * 80)
    print("TIP: Start with Playwright - it's more modern and easier to use!")
    print("=" * 80)
    print()


if __name__ == "__main__":
    main()
