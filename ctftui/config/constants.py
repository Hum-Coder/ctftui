"""Configuration constants"""
import os
from pathlib import Path

CONFIG_DIR = Path.home() / ".ctftui"
CONFIG_FILE = CONFIG_DIR / "config.json"
LOG_FILE = CONFIG_DIR / "ctftui.log"

CONFIG_DIR.mkdir(exist_ok=True)

API_TIMEOUT = 10  # seconds
LEADERBOARD_REFRESH_RATE = 5  # seconds
