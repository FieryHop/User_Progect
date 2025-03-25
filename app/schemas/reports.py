from typing import List

from pydantic import BaseModel


class ReportItem(BaseModel):
    id: int
    hours: float

    class Config:
        schema_extra = {"example": {"id": 1, "hours": 8.5}}


class ReportOut(BaseModel):
    items: List[ReportItem]

    class Config:
        schema_extra = {
            "example": {"items": [{"id": 1, "hours": 12.5}, {"id": 2, "hours": 7.0}]}
        }
