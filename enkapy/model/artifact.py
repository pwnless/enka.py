from typing import List, Optional

from pydantic import BaseModel, Field


class ArtifactProperty(BaseModel):
    mainPropId: str = Field('', alias='mainPropId')
    statValue: float = Field(0, alias='statValue')
    appendPropId: str = Field('', alias='appendPropId')

    @property
    def prop(self) -> str:
        """Artifact property"""
        if self.mainPropId:
            return self.mainPropId
        else:
            return self.appendPropId

    @property
    def value(self) -> float:
        """Artifact property value"""
        return self.statValue


class ArtifactFlat(BaseModel):
    equipType: str
    """Artifact equip types
    
    EQUIP_BRACER: flower
    
    EQUIP_NECKLACE: feather
    
    EQUIP_SHOES: sand
    
    EQUIP_RING: goblet
    
    EQUIP_DRESS: circlet"""
    icon: str
    """Artifact icon"""
    itemType: str
    """Artifact item type, mostly 'ITEM_RELIQUARY'"""
    nameTextMapHash: str
    """Artifact name hash"""
    nameText: Optional[str] = Field('')
    """Artifact name text
    
    *Note: You must called load_lang before otherwise this field is empty*"""
    rankLevel: int
    """Artifact rank, 5/4/3/2/1 star"""
    main_stat: ArtifactProperty = Field({}, alias="reliquaryMainstat")
    """Artifact main stats"""
    sub_stats: List[ArtifactProperty] = Field({}, alias="reliquarySubstats")
    """Artifact sub stats"""
    setNameTextMapHash: str
    """Artifact name hash"""
    setNameText: Optional[str] = Field('')
    """Artifact set name text
    
    *Note: You must called load_lang before otherwise this field is empty*"""

    @property
    def icon_url(self) -> str:
        """
        :return: Artifact icon url from https://enka.shinshin.moe/ui/
        """
        return f'https://enka.network/ui/{self.icon}.png'

    @property
    def name(self):
        return self.nameText

    @property
    def set_name(self):
        return self.setNameText


class ArtifactInfo(BaseModel):
    level: int
    mainPropId: int
    appendPropIdList: Optional[List[int]] = Field([])


class Artifact(BaseModel):
    """Artifact information class"""
    id: int = Field(0, alias="itemId")
    """Artifact id"""
    data: ArtifactInfo = Field({}, alias="reliquary")
    """Some Artifact info like upgrade level, upgrade value etc."""
    flat: ArtifactFlat
    """Artifact flat info class, anything inside flat can be access directly in Artifact class too."""

    @property
    def level(self) -> int:
        """Artifact level"""
        return self.data.level

    def __getattr__(self, item):
        if hasattr(self.flat, item):
            return getattr(self.flat, item)
        else:
            return None
