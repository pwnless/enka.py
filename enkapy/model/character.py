from enum import Enum
from typing import List, Dict, Union, Optional

from pydantic import BaseModel, Field, validator

from .artifact import Artifact
from .combats import CharacterCombat
from .weapon import Weapon


class CharacterPropertyType(int, Enum):
    UNKNOWN = -1
    XP = 1001
    ASCENSION = 1002
    LEVEL = 4001


class CharacterFriendshipLevel(BaseModel):
    level: int = Field(0, alias="expLevel")


class CharacterProperty(BaseModel):
    type: CharacterPropertyType
    ival: str = Field("", alias="ival")
    value: str = Field("", alias="val")

    @validator('type', pre=True)
    def check_type(cls, val: int):
        if val not in [1001, 1002, 4001]:
            val = -1

        return val

    class Config:
        use_enum_values = True


class CharacterInfo(BaseModel):
    name: Optional[str] = Field('')
    id: int = Field(0, alias="avatarId")
    friendship: CharacterFriendshipLevel = Field({}, alias="fetterInfo")
    properties: Dict[str, CharacterProperty] = Field({}, alias="propMap")
    # Artifacts
    equipList: List[Union[Artifact, Weapon]] = Field([], alias="equipList")
    combat: CharacterCombat = Field({}, alias="fightPropMap")
    skill_data: List[int] = Field([], alias="inherentProudSkillList")
    skill_id: int = Field(0, alias="skillDepotId")
    skillDepotId: int
    inherentProudSkillList: List[int]
    skill_level: Dict[int, int] = Field({}, alias="skillLevelMap")

    @property
    def artifacts(self):
        artifacts = []
        for _ in self.equipList:
            if isinstance(_, Artifact):
                artifacts.append(_)
        return artifacts

    @property
    def weapon(self):
        for _ in self.equipList:
            if isinstance(_, Weapon):
                return _
