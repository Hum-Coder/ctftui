"""Pydantic models for CTFd data structures"""
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class Team(BaseModel):
    id: int
    name: str
    points: int
    rank: Optional[int] = None


class User(BaseModel):
    id: int
    name: str
    email: str
    team_id: Optional[int] = None


class Challenge(BaseModel):
    id: int
    name: str
    category: str
    value: int
    description: str
    solved: bool = False
    attempts: Optional[int] = None


class Submission(BaseModel):
    id: int
    challenge_id: int
    provided: str
    correct: bool
    timestamp: datetime


class Leaderboard(BaseModel):
    teams: List[Team]
