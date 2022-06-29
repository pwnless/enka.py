from typing import List

from pydantic import BaseModel, Field

from .character import CharacterInfo
from .players import PlayerInfo


class EnkaData(BaseModel):
    player: PlayerInfo = Field({}, alias="playerInfo")
    characters: List[CharacterInfo] = Field([], alias="avatarInfoList")
    ttl: int = 0
