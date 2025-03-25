from sqlalchemy import Column, Date, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.database import Base


class TimeLog(Base):
    __tablename__ = "timelogs"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    project_id = Column(Integer, ForeignKey("projects.id"))
    hours = Column(Float)
    date_field = Column(Date)

    user = relationship("User", back_populates="timelogs")
    project = relationship("Project", back_populates="timelogs")
