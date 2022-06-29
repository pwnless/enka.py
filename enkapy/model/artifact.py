from typing import List, Optional

from pydantic import BaseModel, Field


class ArtifactProperty(BaseModel):
    mainPropId: str = Field('')
    statValue: int
    appendPropId: str = Field('')

    @property
    def prop(self):
        if self.mainPropId:
            return self.mainPropId
        else:
            return self.appendPropId

    @property
    def value(self):
        return self.statValue


class ArtifactFlat(BaseModel):
    equipType: str
    icon: str
    itemType: str
    nameTextMapHash: str
    nameText: Optional[str] = Field('')
    rankLevel: int
    main_stat: ArtifactProperty = Field({}, alias="reliquaryMainstat")
    sub_stats: List[ArtifactProperty] = Field({}, alias="reliquarySubstats")
    setNameTextMapHash: str
    setNameText: Optional[str] = Field('')


class ArtifactInfo(BaseModel):
    level: int
    mainPropId: int
    appendPropIdList: List[int]


class Artifact(BaseModel):
    id: int = Field(0, alias="itemId")
    data: ArtifactInfo = Field({}, alias="reliquary")
    flat: ArtifactFlat
