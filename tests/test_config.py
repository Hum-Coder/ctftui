"""Tests for configuration"""
import unittest
from pathlib import Path
from ctftui.config.settings import Settings


class TestSettings(unittest.TestCase):
    """Test settings management"""
    
    def setUp(self):
        self.settings = Settings()
    
    def test_cipher_creation(self):
        self.assertIsNotNone(self.settings._cipher)
