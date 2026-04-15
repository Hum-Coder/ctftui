"""Main Textual application"""
from textual.app import ComposeResult
from textual.containers import Container
from textual import on
from textual.widgets import Button
from textual.screen import Screen
from ctftui.ui.app_base import CTFdAppBase
from ctftui.ui.screens.auth import AuthScreen
from ctftui.ui.screens.dashboard import DashboardScreen
from ctftui.config.settings import settings
import logging

logger = logging.getLogger(__name__)


class CTFdApp(CTFdAppBase):
    """Main CTFd TUI application"""
    
    def on_mount(self) -> None:
        """Check if authenticated and show appropriate screen"""
        config = settings.load_config()
        
        if config:
            # Already authenticated, show dashboard
            self.push_screen(DashboardScreen())
        else:
            # Not authenticated, show login
            self.push_screen(AuthScreen())
