from enum import Enum
from typing import List, Dict, Union, Optional

from pydantic import BaseModel, Field, validator

from .artifact import Artifact
from .combats import CharacterCombat
from .weapon import Weapon


class CharacterPropertyType(int, Enum):
    """ """
    UNKNOWN = -1
    XP = 1001
    ASCENSION = 1002
    LEVEL = 4001


class CharacterFriendshipLevel(BaseModel):
    """ """
    level: int = Field(0, alias="expLevel")


class CharacterProperty(BaseModel):
    """ """
    type: CharacterPropertyType
    ival: str = Field("", alias="ival")
    value: str = Field("", alias="val")

    @validator('type', pre=True)
    def check_type(cls, val: int):
        if val not in [1001, 1002, 4001]:
            val = -1

        return val

    class Config:
        """ """
        use_enum_values = True


class CharacterInfo(BaseModel):
    """
    Character info class for every character shown in game
    """
    name: Optional[str] = Field('')
    """Character name"""
    id: int = Field(0, alias="avatarId")
    "Character avatar id for fetching more detail later"
    friendship: CharacterFriendshipLevel = Field({}, alias="fetterInfo")
    "Character friendship"
    properties: Dict[str, CharacterProperty] = Field({}, alias="propMap")
    "Some character properties like xp, ascension , level"
    # Artifacts
    equipList: List[Union[Artifact, Weapon]] = Field([], alias="equipList")
    "Everything equipped on character, including artifacts and weapon"
    combat: CharacterCombat = Field({}, alias="fightPropMap")
    "Character combat stats"
    skill_data: List[int] = Field([], alias="inherentProudSkillList")
    "Character skill data"
    skill_id: int = Field(0, alias="skillDepotId")
    talents: List[int] = Field([], alias='talentIdList')
    """Character talents"""
    skillDepotId: int
    inherentProudSkillList: List[int]
    skill_level: Dict[int, int] = Field({}, alias="skillLevelMap")
    """Character skill level map, skill_id:skill_level"""

    @property
    def artifacts(self) -> List[Artifact]:
        """
        :return: Artifact lists equipped on character
        """
        artifacts = []
        for _ in self.equipList:
            if isinstance(_, Artifact):
                artifacts.append(_)
        return artifacts

    @property
    def weapon(self) -> Weapon:
        """
        :return: weapon equipped on character
        """
        for _ in self.equipList:
            if isinstance(_, Weapon):
                return _
