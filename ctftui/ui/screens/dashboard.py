"""Main dashboard screen with tabs"""
from textual.containers import Container
from textual.screen import Screen
from textual.widgets import Static, TabbedContent, TabPane
from ctftui.ui.screens.leaderboard import LeaderboardWidget
from ctftui.ui.screens.challenges import ChallengesWidget
from ctftui.ui.screens.submissions import SubmissionsWidget


class DashboardScreen(Screen):
    """Main dashboard with multiple tabs"""
    
    BINDINGS = [
        ("q", "quit", "Quit"),
        ("1", "leaderboard_tab", "Leaderboard"),
        ("2", "challenges_tab", "Challenges"),
        ("3", "submissions_tab", "Submissions"),
    ]
    
    def compose(self):
        """Create dashboard layout"""
        with TabbedContent(initial="leaderboard"):
            with TabPane("Leaderboard", id="leaderboard"):
                yield LeaderboardWidget()
            with TabPane("Challenges", id="challenges"):
                yield ChallengesWidget()
            with TabPane("Submissions", id="submissions"):
                yield SubmissionsWidget()
