from pydantic import BaseModel, ConfigDict


class ProjectBase(BaseModel):
    name: str


class ProjectCreate(ProjectBase):
    manager_id: int


class ProjectUpdate(BaseModel):
    name: str | None = None
    manager_id: int | None = None


class Project(ProjectBase):
    id: int
    manager_id: int

    model_config = ConfigDict(from_attributes=True)
