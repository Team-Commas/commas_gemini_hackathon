#!/usr/bin/env python3
"""
Browser Tab Screenshot Analyzer
Captures browser tab screenshots and extracts structured data using Gemini 3 Flash
"""

from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from typing import List, Optional
import base64
from pathlib import Path


# Define the schema for browser tab data extraction
class FormField(BaseModel):
    """Represents a form field in the browser"""
    label: str = Field(description="The label or placeholder text of the field")
    field_type: str = Field(description="Type of field (text, email, password, select, etc.)")
    value: Optional[str] = Field(default=None, description="Current value if visible")
    required: bool = Field(default=False, description="Whether the field is required")


class Button(BaseModel):
    """Represents a button or clickable element"""
    text: str = Field(description="Button text or label")
    button_type: str = Field(description="Type (submit, button, link, etc.)")
    primary: bool = Field(default=False, description="Whether it's a primary action button")


class BrowserTabSchema(BaseModel):
    """Complete schema for browser tab analysis"""
    page_title: str = Field(description="Title of the page")
    url: Optional[str] = Field(default=None, description="URL if visible in screenshot")
    main_heading: Optional[str] = Field(default=None, description="Main heading or title on the page")
    form_fields: List[FormField] = Field(default_factory=list, description="All form fields found")
    buttons: List[Button] = Field(default_factory=list, description="All buttons found")
    links: List[str] = Field(default_factory=list, description="Visible navigation links")
    error_messages: List[str] = Field(default_factory=list, description="Any error or warning messages")
    page_type: str = Field(description="Type of page (login, signup, dashboard, form, etc.)")
    description: str = Field(description="Brief description of what the page does")


class ScreenshotAnalyzer:
    """Analyzes browser screenshots using Gemini 3 Flash"""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the analyzer
        
        Args:
            api_key: Optional API key. If not provided, uses GEMINI_API_KEY env var
        """
        if api_key:
            self.client = genai.Client(api_key=api_key)
        else:
            self.client = genai.Client()
    
    def analyze_screenshot(self, image_path: str, use_v1alpha: bool = False) -> dict:
        """
        Analyze a browser screenshot and extract structured data
        
        Args:
            image_path: Path to the screenshot image file
            use_v1alpha: Whether to use v1alpha API for media_resolution parameter
            
        Returns:
            Dictionary containing extracted data matching BrowserTabSchema
        """
        # Read the image file
        with open(image_path, 'rb') as f:
            image_bytes = f.read()
        
        # Determine MIME type
        suffix = Path(image_path).suffix.lower()
        mime_types = {
            '.jpg': 'image/jpeg',
            '.jpeg': 'image/jpeg',
            '.png': 'image/png',
            '.webp': 'image/webp',
            '.gif': 'image/gif'
        }
        mime_type = mime_types.get(suffix, 'image/png')
        
        # Create the prompt
        prompt = """Analyze this browser tab screenshot and extract all visible information.
        
Focus on:
- Page title and main heading
- All form fields (labels, types, whether required)
- All buttons and their purposes
- Navigation links
- Any error or warning messages
- The overall purpose and type of the page

Be thorough and accurate. Extract exactly what you see."""
        
        # Prepare the content parts
        if use_v1alpha:
            # Use v1alpha API with media_resolution parameter
            client_alpha = genai.Client(http_options={'api_version': 'v1alpha'})
            
            response = client_alpha.models.generate_content(
                model="gemini-3-flash-preview",
                contents=[
                    types.Content(
                        parts=[
                            types.Part(text=prompt),
                            types.Part(
                                inline_data=types.Blob(
                                    mime_type=mime_type,
                                    data=image_bytes,
                                ),
                                media_resolution={"level": "media_resolution_high"}
                            )
                        ]
                    )
                ],
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_json_schema=BrowserTabSchema.model_json_schema(),
                    thinking_config=types.ThinkingConfig(thinking_level="low")
                )
            )
        else:
            # Use standard API without media_resolution
            response = self.client.models.generate_content(
                model="gemini-3-flash-preview",
                contents=[
                    prompt,
                    types.Part.from_bytes(
                        data=image_bytes,
                        mime_type=mime_type,
                    )
                ],
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_json_schema=BrowserTabSchema.model_json_schema(),
                    thinking_config=types.ThinkingConfig(thinking_level="low")
                )
            )
        
        # Parse and validate the response
        result = BrowserTabSchema.model_validate_json(response.text)
        return result.model_dump()
    
    def analyze_from_base64(self, base64_image: str, mime_type: str = "image/png") -> dict:
        """
        Analyze a browser screenshot from base64 encoded string
        
        Args:
            base64_image: Base64 encoded image string
            mime_type: MIME type of the image
            
        Returns:
            Dictionary containing extracted data matching BrowserTabSchema
        """
        # Decode base64 to bytes
        image_bytes = base64.b64decode(base64_image)
        
        prompt = """Analyze this browser tab screenshot and extract all visible information.
        
Focus on:
- Page title and main heading
- All form fields (labels, types, whether required)
- All buttons and their purposes
- Navigation links
- Any error or warning messages
- The overall purpose and type of the page

Be thorough and accurate. Extract exactly what you see."""
        
        response = self.client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=[
                prompt,
                types.Part.from_bytes(
                    data=image_bytes,
                    mime_type=mime_type,
                )
            ],
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_json_schema=BrowserTabSchema.model_json_schema(),
                thinking_config=types.ThinkingConfig(thinking_level="low")
            )
        )
        
        result = BrowserTabSchema.model_validate_json(response.text)
        return result.model_dump()


def main():
    """Example usage"""
    import sys
    import json
    
    if len(sys.argv) < 2:
        print("Usage: python screenshot_analyzer.py <path_to_screenshot>")
        print("Example: python screenshot_analyzer.py screenshot.png")
        sys.exit(1)
    
    image_path = sys.argv[1]
    
    if not Path(image_path).exists():
        print(f"Error: File '{image_path}' not found")
        sys.exit(1)
    
    print(f"Analyzing screenshot: {image_path}")
    print("Using Gemini 3 Flash with high resolution image processing...")
    print()
    
    analyzer = ScreenshotAnalyzer()
    
    try:
        result = analyzer.analyze_screenshot(image_path)
        
        # Pretty print the JSON result
        print("=" * 80)
        print("EXTRACTED DATA (JSON):")
        print("=" * 80)
        print(json.dumps(result, indent=2))
        
        # Save to file
        output_file = Path(image_path).stem + "_analysis.json"
        with open(output_file, 'w') as f:
            json.dump(result, f, indent=2)
        
        print()
        print(f"✓ Analysis saved to: {output_file}")
        
    except Exception as e:
        print(f"Error analyzing screenshot: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
