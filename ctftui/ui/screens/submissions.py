"""Submissions history widget"""
from textual.widgets import Widget, DataTable


class SubmissionsWidget(Widget):
    """Display submission history"""
    
    DEFAULT_CSS = """
    SubmissionsWidget {
        width: 100%;
        height: 100%;
    }
    """
    
    def compose(self):
        yield DataTable(id="submissions_table")
    
    def on_mount(self):
        """Initialize submissions table""" 
        table = self.query_one(DataTable)
        table.add_columns("Challenge", "Status", "Time")
        
        # Placeholder data
        table.add_row("Challenge 2", "✓ Correct", "2026-04-15 10:30")
