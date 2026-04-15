"""CTFd API client"""
import logging
import requests
from typing import Optional, List
from ctftui.api.models import Team, User, Challenge, Submission, Leaderboard
from ctftui.api.exceptions import AuthenticationError, RateLimitError, ConnectionError as CTFdConnectionError

logger = logging.getLogger(__name__)


class CTFdClient:
    """Client for interacting with CTFd API"""
    
    def __init__(self, base_url: str, api_key: str, timeout: int = 10):
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': f'Token {api_key}',
            'Content-Type': 'application/json',
        })
    
    def _request(self, method: str, endpoint: str, **kwargs):
        """Make API request"""
        url = f"{self.base_url}/api/v1{endpoint}"
        kwargs.setdefault('timeout', self.timeout)
        
        try:
            response = self.session.request(method, url, **kwargs)
            
            if response.status_code == 401:
                raise AuthenticationError("Invalid API key")
            elif response.status_code == 429:
                raise RateLimitError("Rate limit exceeded")
            elif response.status_code >= 400:
                raise CTFdConnectionError(f"API error: {response.status_code}")
            
            return response.json()
        except requests.RequestException as e:
            raise CTFdConnectionError(f"Connection failed: {e}")
    
    def verify_auth(self) -> bool:
        """Verify authentication"""
        try:
            self._request('GET', '/users/me')
            return True
        except Exception as e:
            logger.error(f"Auth verification failed: {e}")
            return False
    
    def get_user(self) -> Optional[User]:
        """Get current user info"""
        try:
            data = self._request('GET', '/users/me')
            return User(**data['data'])
        except Exception as e:
            logger.error(f"Failed to get user: {e}")
            return None
    
    def get_leaderboard(self) -> Optional[Leaderboard]:
        """Get leaderboard"""
        try:
            data = self._request('GET', '/scoreboard')
            teams = [Team(**team) for team in data['data']]
            return Leaderboard(teams=teams)
        except Exception as e:
            logger.error(f"Failed to get leaderboard: {e}")
            return None
    
    def get_challenges(self) -> Optional[List[Challenge]]:
        """Get all challenges"""
        try:
            data = self._request('GET', '/challenges')
            return [Challenge(**challenge) for challenge in data['data']]
        except Exception as e:
            logger.error(f"Failed to get challenges: {e}")
            return None
    
    def get_challenge(self, challenge_id: int) -> Optional[Challenge]:
        """Get specific challenge"""
        try:
            data = self._request('GET', f'/challenges/{challenge_id}')
            return Challenge(**data['data'])
        except Exception as e:
            logger.error(f"Failed to get challenge: {e}")
            return None
    
    def submit_flag(self, challenge_id: int, flag: str) -> bool:
        """Submit a flag"""
        try:
            data = self._request(
                'POST',
                f'/challenges/{challenge_id}/attempts',
                json={'submission': flag}
            )
            return data.get('data', {}).get('correct', False)
        except Exception as e:
            logger.error(f"Failed to submit flag: {e}")
            return False
