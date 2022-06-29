from typing import List

from pydantic import BaseModel


class ProfilePicture(BaseModel):
    avatarId: int


class ShowAvatar(BaseModel):
    avatarId: str
    level: int


class PlayerInfo(BaseModel):
    # Profile info
    finishAchievementNum: int
    level: int
    nameCardId: int
    nickname: str
    signature: str
    worldLevel: int
    profilePicture: ProfilePicture
    # Avatars
    showAvatarInfoList: List[ShowAvatar]
    # Abyss floor
    towerFloorIndex: int
    towerLevelIndex: int
