"""Leaderboard widget"""
from textual.widgets import Widget, DataTable
from textual.containers import Container, Vertical
import asyncio


class LeaderboardWidget(Widget):
    """Display CTFd leaderboard"""
    
    DEFAULT_CSS = """
    LeaderboardWidget {
        width: 100%;
        height: 100%;
    }
    """
    
    def compose(self):
        yield DataTable(id="leaderboard_table")
    
    def on_mount(self):
        """Initialize leaderboard table""" 
        table = self.query_one(DataTable)
        table.add_columns("Rank", "Team", "Points", "Solves")
        
        # Placeholder data
        table.add_row("1", "Your Team", "1000", "5")
        table.add_row("2", "Other Team", "950", "4")
