from typing import Dict, List, Optional

from pydantic import BaseModel, Field


class WeaponInfo(BaseModel):
    level: int
    affixMap: Dict[int, int]
    promoteLevel: int


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
    id: int = Field(0, alias="itemId")
    data: WeaponInfo = Field({}, alias="weapon")
    flat: WeaponFlat = Field({})
