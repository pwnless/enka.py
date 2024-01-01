from typing import List, Optional

from pydantic import BaseModel


class ProfilePicture(BaseModel):
    avatarId1: Optional[int] = Field(0, alias='id')
    avatarId2: Optional[int] = Field(0, alias='avatarId')

    @property
    def avatarId(self):
        if self.avatarId1:
            return self.avatarId1
        elif self.avatarId2:
            return self.avatarId2
        else:
            return 0



class ShowAvatar(BaseModel):
    avatarId: int
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
    signature: Optional[str] = ''
    """Player signature"""
    worldLevel: Optional[int]
    """Player world level"""
    profilePicture: ProfilePicture
    """Player profile picture"""

    showAvatarInfoList: Optional[List[ShowAvatar]] = []
    """Player characters shown"""

    towerFloorIndex: Optional[int]
    """Player abyss floor"""
    towerLevelIndex: Optional[int]
    """Player abyss level"""
