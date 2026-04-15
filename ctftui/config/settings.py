"""Configuration and credential management"""
import json
import logging
from pathlib import Path
from cryptography.fernet import Fernet
from ctftui.config.constants import CONFIG_FILE, CONFIG_DIR

logger = logging.getLogger(__name__)


class Settings:
    """Manage app settings and credentials"""
    
    def __init__(self):
        self.config_file = CONFIG_FILE
        self.key_file = CONFIG_DIR / ".key"
        self._cipher = self._get_or_create_cipher()
    
    def _get_or_create_cipher(self):
        """Get or create encryption cipher"""
        if self.key_file.exists():
            with open(self.key_file, 'rb') as f:
                key = f.read()
        else:
            key = Fernet.generate_key()
            with open(self.key_file, 'wb') as f:
                f.write(key)
        return Fernet(key)
    
    def load_config(self):
        """Load configuration from file"""
        if not self.config_file.exists():
            return None
        
        try:
            with open(self.config_file, 'r') as f:
                config = json.load(f)
            
            if 'api_key' in config:
                config['api_key'] = self._cipher.decrypt(
                    config['api_key'].encode()
                ).decode()
            
            return config
        except Exception as e:
            logger.error(f"Failed to load config: {e}")
            return None
    
    def save_config(self, base_url: str, api_key: str):
        """Save configuration with encrypted API key"""
        try:
            encrypted_key = self._cipher.encrypt(api_key.encode()).decode()
            config = {
                'base_url': base_url,
                'api_key': encrypted_key,
            }
            
            with open(self.config_file, 'w') as f:
                json.dump(config, f)
            
            logger.info("Configuration saved successfully")
        except Exception as e:
            logger.error(f"Failed to save config: {e}")
            raise
    
    def clear_credentials(self):
        """Clear stored credentials"""
        if self.config_file.exists():
            self.config_file.unlink()
            logger.info("Credentials cleared")


settings = Settings()
