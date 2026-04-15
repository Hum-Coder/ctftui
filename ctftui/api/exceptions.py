"""Custom API exceptions"""


class CTFdAPIError(Exception):
    """Base exception for CTFd API errors"""
    pass


class AuthenticationError(CTFdAPIError):
    """Authentication failed"""
    pass

class RateLimitError(CTFdAPIError):
    """Rate limit exceeded"""
    pass

class ConnectionError(CTFdAPIError):
    """Connection to CTFd failed"""
    pass
