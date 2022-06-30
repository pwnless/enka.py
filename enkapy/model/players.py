from typing import List,Optional

from pydantic import BaseModel


class ProfilePicture(BaseModel):
    avatarId: int


class ShowAvatar(BaseModel):
    avatarId: str
    level: int


class PlayerInfo(BaseModel):
    # Profile info
    finishAchievementNum: Optional[int]
    level: int
    nameCardId: int
    nickname: str
    signature: Optional[str]
    worldLevel: Optional[int]
    profilePicture: ProfilePicture
    # Avatars
    showAvatarInfoList: Optional[List[ShowAvatar]]
    # Abyss floor
    towerFloorIndex: Optional[int]
    towerLevelIndex: Optional[int]
