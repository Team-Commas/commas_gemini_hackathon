// API Key management
let apiKey = null;

// Load saved API key when popup opens
document.addEventListener('DOMContentLoaded', () => {
  chrome.storage.local.get(['geminiApiKey'], (result) => {
    if (result.geminiApiKey) {
      apiKey = result.geminiApiKey;
      document.getElementById('apiKeyInput').value = '••••••••';
      document.getElementById('analyzeBtn').disabled = false;
      document.getElementById('apiKeySection').style.display = 'none';
      console.log('API key loaded from storage');
    } else {
      console.log('No API key found in storage');
    }
  });
});

// Save API key
document.getElementById('saveKeyBtn').addEventListener('click', () => {
  const input = document.getElementById('apiKeyInput');
  const key = input.value.trim();
  
  if (!key) {
    showStatus('Please enter an API key', 'error');
    return;
  }
  
  if (key === '••••••••') {
    showStatus('API key already saved', 'info');
    return;
  }
  
  console.log('Saving API key...');
  
  chrome.storage.local.set({ geminiApiKey: key }, () => {
    if (chrome.runtime.lastError) {
      console.error('Error saving API key:', chrome.runtime.lastError);
      showStatus('Error saving API key: ' + chrome.runtime.lastError.message, 'error');
      return;
    }
    
    apiKey = key;
    input.value = '••••••••';
    document.getElementById('analyzeBtn').disabled = false;
    document.getElementById('apiKeySection').style.display = 'none';
    showStatus('API key saved successfully!', 'success');
    console.log('API key saved successfully');
  });
});

// Toggle API key visibility
document.getElementById('toggleKeyBtn').addEventListener('click', () => {
  const input = document.getElementById('apiKeyInput');
  if (input.type === 'password') {
    input.type = 'text';
  } else {
    input.type = 'password';
  }
});

// Analyze button
document.getElementById('analyzeBtn').addEventListener('click', async () => {
  showStatus('Capturing screenshot...', 'info');
  document.getElementById('analyzeBtn').disabled = true;
  
  try {
    // Get active tab
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    
    // Capture screenshot
    const dataUrl = await chrome.tabs.captureVisibleTab(null, {
      format: 'png',
      quality: 100
    });
    
    showStatus('Analyzing with Gemini AI...', 'info');
    
    // Convert data URL to base64
    const base64Image = dataUrl.split(',')[1];
    
    // Call Gemini API
    const result = await analyzeWithGemini(base64Image);
    
    // Display results
    displayResults(result);
    showStatus('Analysis complete!', 'success');
    
  } catch (error) {
    console.error('Error:', error);
    showStatus(`Error: ${error.message}`, 'error');
  } finally {
    document.getElementById('analyzeBtn').disabled = false;
  }
});

async function analyzeWithGemini(base64Image) {
  const prompt = `Analyze this browser tab screenshot and extract all visible information.

Focus on:
- Page title and main heading
- All form fields (labels, types, whether required)
- All buttons and their purposes
- Navigation links
- Any error or warning messages
- The overall purpose and type of the page

Be thorough and accurate. Extract exactly what you see.`;

  const response = await fetch('https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'x-goog-api-key': apiKey
    },
    body: JSON.stringify({
      contents: [{
        parts: [
          { text: prompt },
          {
            inline_data: {
              mime_type: 'image/png',
              data: base64Image
            }
          }
        ]
      }],
      generationConfig: {
        response_mime_type: 'application/json',
        response_schema: {
          type: 'object',
          properties: {
            page_title: { type: 'string', description: 'Title of the page' },
            url: { type: 'string', nullable: true, description: 'URL if visible' },
            main_heading: { type: 'string', nullable: true, description: 'Main heading' },
            form_fields: {
              type: 'array',
              items: {
                type: 'object',
                properties: {
                  label: { type: 'string' },
                  field_type: { type: 'string' },
                  value: { type: 'string', nullable: true },
                  required: { type: 'boolean' }
                },
                required: ['label', 'field_type', 'required']
              }
            },
            buttons: {
              type: 'array',
              items: {
                type: 'object',
                properties: {
                  text: { type: 'string' },
                  button_type: { type: 'string' },
                  primary: { type: 'boolean' }
                },
                required: ['text', 'button_type', 'primary']
              }
            },
            links: { type: 'array', items: { type: 'string' } },
            error_messages: { type: 'array', items: { type: 'string' } },
            page_type: { type: 'string' },
            description: { type: 'string' }
          },
          required: ['page_title', 'page_type', 'description']
        }
      }
    })
  });

  if (!response.ok) {
    const error = await response.json();
    throw new Error(error.error?.message || 'API request failed');
  }

  const data = await response.json();
  const text = data.candidates[0].content.parts[0].text;
  return JSON.parse(text);
}

function displayResults(data) {
  const resultsDiv = document.getElementById('results');
  resultsDiv.classList.remove('hidden');
  
  let html = '';
  
  // Page info
  html += `
    <div class="result-section">
      <h3>Page Information</h3>
      <div class="result-value"><strong>${data.page_title}</strong></div>
      ${data.main_heading ? `<div class="result-value">${data.main_heading}</div>` : ''}
      <div class="result-value" style="color: #666; font-size: 14px;">${data.page_type}</div>
      <div class="result-value" style="font-size: 14px; margin-top: 8px;">${data.description}</div>
    </div>
  `;
  
  // Form fields
  if (data.form_fields && data.form_fields.length > 0) {
    html += `
      <div class="result-section">
        <h3>Form Fields (${data.form_fields.length})</h3>
    `;
    data.form_fields.forEach(field => {
      html += `
        <div class="field-item">
          <span class="field-label">${field.label}</span>
          <span class="field-type">${field.field_type}</span>
          ${field.required ? '<span class="required-badge">REQUIRED</span>' : ''}
          ${field.value ? `<div style="font-size: 12px; color: #666; margin-top: 4px;">Value: ${field.value}</div>` : ''}
        </div>
      `;
    });
    html += `</div>`;
  }
  
  // Buttons
  if (data.buttons && data.buttons.length > 0) {
    html += `
      <div class="result-section">
        <h3>Buttons (${data.buttons.length})</h3>
    `;
    data.buttons.forEach(button => {
      html += `
        <div class="button-item">
          <span class="field-label">${button.text}</span>
          <span class="field-type">${button.button_type}</span>
          ${button.primary ? '<span class="primary-badge">PRIMARY</span>' : ''}
        </div>
      `;
    });
    html += `</div>`;
  }
  
  // Links
  if (data.links && data.links.length > 0) {
    html += `
      <div class="result-section">
        <h3>Links (${data.links.length})</h3>
    `;
    data.links.forEach(link => {
      html += `<div class="link-item">${link}</div>`;
    });
    html += `</div>`;
  }
  
  // Error messages
  if (data.error_messages && data.error_messages.length > 0) {
    html += `
      <div class="result-section">
        <h3>Error Messages</h3>
    `;
    data.error_messages.forEach(msg => {
      html += `<div class="error-message">${msg}</div>`;
    });
    html += `</div>`;
  }
  
  // JSON view
  html += `
    <div class="result-section">
      <h3>Raw JSON</h3>
      <div class="json-view">${JSON.stringify(data, null, 2)}</div>
      <button class="copy-btn" id="copyJsonBtn">Copy JSON</button>
    </div>
  `;
  
  resultsDiv.innerHTML = html;
  
  // Add copy functionality
  document.getElementById('copyJsonBtn').addEventListener('click', () => {
    navigator.clipboard.writeText(JSON.stringify(data, null, 2));
    showStatus('JSON copied to clipboard!', 'success');
  });
}

function showStatus(message, type) {
  const statusDiv = document.getElementById('status');
  statusDiv.textContent = message;
  statusDiv.className = `status ${type}`;
  statusDiv.classList.remove('hidden');
  
  if (type === 'success') {
    setTimeout(() => {
      statusDiv.classList.add('hidden');
    }, 3000);
  }
}
