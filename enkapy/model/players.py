from typing import List, Optional

from pydantic import BaseModel


class ProfilePicture(BaseModel):
    avatarId: Optional[int]


class ShowAvatar(BaseModel):
    avatarId: str
    """Character id"""
    level: int
    """Character level"""


class PlayerInfo(BaseModel):
    """
    Player info class
    """
    finishAchievementNum: Optional[int]
    """Total achievement"""
    level: int
    """Player level"""
    nameCardId: int
    """Player name card background id"""
    nickname: Optional[str]
    """Player nickname"""
    signature: Optional[str]
    """Player signature"""
    worldLevel: Optional[int]
    """Player world level"""
    profilePicture: ProfilePicture
    """Player profile picture"""

    showAvatarInfoList: Optional[List[ShowAvatar]]
    """Player characters shown"""

    towerFloorIndex: Optional[int]
    """Player abyss floor"""
    towerLevelIndex: Optional[int]
    """Player abyss level"""
