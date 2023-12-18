from typing import List, Optional

from pydantic import BaseModel, Field

from .character import CharacterInfo
from .players import PlayerInfo


class EnkaData(BaseModel):
    """All data about the player"""
    player: PlayerInfo = Field({}, alias="playerInfo")
    """Basic player info"""
    characters: Optional[List[CharacterInfo]] = Field([], alias="avatarInfoList")
    """Player characters shown in game"""
    ttl: int = 0
