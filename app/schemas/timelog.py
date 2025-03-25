from datetime import date

from pydantic import BaseModel, ConfigDict


class TimeLogBase(BaseModel):
    user_id: int
    project_id: int
    hours: float
    date_field: date


class TimeLogCreate(TimeLogBase):
    pass


class TimeLogUpdate(BaseModel):
    user_id: int | None = None
    project_id: int | None = None
    hours: float | None = None
    date_field: date | None = None


class TimeLog(TimeLogBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
