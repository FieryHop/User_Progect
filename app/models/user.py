from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    role = Column(String)
    manager_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    projects = relationship("Project", back_populates="manager")
    timelogs = relationship("TimeLog", back_populates="user")
