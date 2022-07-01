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


class Weapon(BaseModel):
    """Weapon info class"""
    id: int = Field(0, alias="itemId")
    """Weapon id"""
    data: WeaponInfo = Field({}, alias="weapon")
    """Weapon data"""
    flat: WeaponFlat = Field({})
    """Weapon flat data, anything inside flat can be access directly in Weapon class too."""

    @property
    def level(self):
        """Weapon level"""
        return self.data.level

    def __getattr__(self, item):
        if hasattr(self.flat, item):
            return getattr(self.flat, item)
        else:
            return None
