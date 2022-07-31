from typing import Dict, List, Optional

from pydantic import BaseModel, Field


class WeaponInfo(BaseModel):
    level: int
    affixMap: Optional[Dict[int, int]]
    promoteLevel: Optional[int]


class WeaponStats(BaseModel):
    appendPropId: str
    statValue: int


class WeaponFlat(BaseModel):
    icon: str
    itemType: str
    nameTextMapHash: str
    nameText: Optional[str] = Field('')
    rankLevel: int
    weaponStats: List[WeaponStats]

    @property
    def name(self):
        return self.nameText

    @property
    def rank(self):
        return self.rankLevel


class Weapon(BaseModel):
    """Weapon info class"""
    id: int = Field(0, alias="itemId")
    """Weapon id"""
    data: WeaponInfo = Field({}, alias="weapon")
    """Weapon data"""
    flat: WeaponFlat = Field({})
    """Weapon flat data, anything inside flat can be access directly in Weapon class too."""

    @property
    def level(self) -> int:
        """Weapon level"""
        return self.data.level

    @property
    def refine(self) -> int:
        for key, val in self.data.affixMap.items():
            if val:
                return val + 1
        return 0

    def __getattr__(self, item):
        if hasattr(self.flat, item):
            return getattr(self.flat, item)
        else:
            return None
