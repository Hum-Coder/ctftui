"""Challenges widget"""
from textual.widgets import Widget, DataTable


class ChallengesWidget(Widget):
    """Display available challenges"""
    
    DEFAULT_CSS = """
    ChallengesWidget {
        width: 100%;
        height: 100%;
    }
    """
    
    def compose(self):
        yield DataTable(id="challenges_table")
    
    def on_mount(self):
        """Initialize challenges table""" 
        table = self.query_one(DataTable)
        table.add_columns("Name", "Category", "Points", "Solved")
        
        # Placeholder data
        table.add_row("Challenge 1", "Web", "100", "No")
        table.add_row("Challenge 2", "Crypto", "200", "Yes")
