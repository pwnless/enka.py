from typing import List

from pydantic import BaseModel, Field

from .character import CharacterInfo
from .players import PlayerInfo


class EnkaData(BaseModel):
    """All data about the player"""
    player: PlayerInfo = Field({}, alias="playerInfo")
    """Basic player info"""
    characters: List[CharacterInfo] = Field([], alias="avatarInfoList")
    """Player characters shown in game"""
    ttl: int = 0
