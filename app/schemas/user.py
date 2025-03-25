from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    username: str
    role: str


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    username: str | None = None
    role: str | None = None


class User(UserBase):
    id: int
    manager_id: int | None = None

    model_config = ConfigDict(from_attributes=True)
