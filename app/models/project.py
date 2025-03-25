from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    manager_id = Column(Integer, ForeignKey("users.id"))

    manager = relationship("User", back_populates="projects")
    timelogs = relationship("TimeLog", back_populates="project")
