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


class CharacterConstellation:
    name = ''
    icon = ''
    id = 0
    name_hash = 0
    activated = False


class CharacterSkillType(int, Enum):
    NormalSkill = 0
    ElementalSkill = 1
    ElementalBurst = 2


class CharacterSkill:
    name = ''
    level = 0
    icon = ''
    id = 0
    name_hash = 0
    type: CharacterSkillType


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
    inherentProudSkillList: List[int] = Field([], alias="inherentProudSkillList")
    "Character skill data"
    skill_depot_id: int = Field(0, alias="skillDepotId")
    """Character skill depot id"""
    internal_constellations: List[int] = Field([], alias='talentIdList')
    """Internal Character talents"""
    constellations: Optional[List[CharacterConstellation]] = Field([])
    """Character talents"""
    skill_level: Dict[int, int] = Field({}, alias="skillLevelMap")
    """Character skill level map, skill_id:skill_level"""
    skills: Optional[List[CharacterSkill]] = Field([])
    """Character skill info"""

    @property
    def ascension(self):
        for key, val in self.properties.items():
            if int(key) == CharacterPropertyType.ASCENSION:
                return val.ival
        return 0

    @property
    def level(self):
        for key, val in self.properties.items():
            if int(key) == CharacterPropertyType.LEVEL:
                return val.ival
        return 0

    @property
    def experience(self):
        for key, val in self.properties.items():
            if int(key) == CharacterPropertyType.XP:
                return val.ival
        return 0

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

    def activate_constellation(self):
        for c in self.constellations:
            if c.id in self.internal_constellations:
                c.activated = True

    def process_skill(self):
        for s in self.skills:
            if s.id in self.skill_level:
                s.level = self.skill_level[s.id]

    class Config:
        arbitrary_types_allowed = True
