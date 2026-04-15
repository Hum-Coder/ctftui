# BYOK.md - Bring Your Own Key Documentation

## Getting CTFd API Key

1. Navigate to the CTFd Settings panel.
2. Locate the API section.
3. Click on "Generate API Key" and copy your API key.

## First Launch Setup

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/Hum-Coder/ctftui.git
   cd ctftui
   ```
2. Install all necessary dependencies using your package manager.
3. Configure the initial settings in `config.json` or relevant configuration files.
4. Run the application with:
   ```bash
   python app.py
   ```

## Managing Multiple Keys

- To manage multiple API keys, create a dedicated section in your `config.json`:
```json
{
  "api_keys": [
    "key1",
    "key2",
    "key3"
  ]
}
```
- Retrieve keys dynamically based on your needs during application runtime.

## Security Information

- Always keep your API keys confidential.
- Avoid hardcoding keys in your source code; use environment variables instead.
- Regularly rotate your API keys to minimize potential abuse.

## Troubleshooting

- **Issue**: API key not working.
  - **Solution**: Double-check the key for typos or expiration.
- **Issue**: Application not launching.
  - **Solution**: Ensure all dependencies are correctly installed and configurations are properly set up.

---
*Note: Always refer to the official CTFd documentation for the most up-to-date information regarding API usage and best practices.*