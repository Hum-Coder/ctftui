"""Tests for API client"""
import unittest
from unittest.mock import Mock, patch
from ctftui.api.client import CTFdClient


class TestCTFdClient(unittest.TestCase):
    """Test CTFd API client"""
    
    def setUp(self):
        self.client = CTFdClient('https://ctf.example.com', 'test_key')
    
    def test_initialization(self):
        self.assertEqual(self.client.base_url, 'https://ctf.example.com')
        self.assertEqual(self.client.api_key, 'test_key')
