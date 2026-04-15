"""Authentication screen"""

import logging
from textual.containers import Container, Vertical, Horizontal
from textual.widgets import Static, Input, Button, Label
from textual.screen import Screen

logger = logging.getLogger(__name__)


class AuthScreen(Screen):
    """Authentication/Login screen"""
    
    BINDINGS = [
        ("escape", "back", "Back"),
    ]
    
    def compose(self):
        """Create authentication form"""
        yield Vertical(
            Static("CTFd TUI - Authentication", id="title"),
            Static("Enter your CTFd instance details", id="subtitle"),
            Vertical(
                Label("CTFd Instance URL"),
                Input(id="base_url", placeholder="https://ctf.example.com"),
                Label("API Key"),
                Input(id="api_key", placeholder="Your CTFd API key", password=True),
                Horizontal(
                    Button("Login", id="login_btn", variant="primary"),
                    Button("Cancel", id="cancel_btn"),
                ),
                id="form",
            ),
            id="auth_container",
        )
