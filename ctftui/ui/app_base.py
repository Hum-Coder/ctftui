"""Base Textual application"""
from textual.app import App, ComposeResult
from ctftui.ui.styles import STYLES


class CTFdAppBase(App):
    """Base CTFd application"""
    
    CSS = STYLES
    TITLE = "CTFd TUI"
    SUB_TITLE = "Terminal interface for CTF challenges"
    
    def compose(self) -> ComposeResult:
        yield from super().compose()
