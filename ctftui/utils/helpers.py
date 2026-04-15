"""Utility helper functions"""

def format_points(points: int) -> str:
    """Format points with comma separator"""
    return f"{points:,}"


def format_timestamp(timestamp: str) -> str:
    """Format timestamp for display"""
    return timestamp.split('T')[0] if 'T' in timestamp else timestamp
