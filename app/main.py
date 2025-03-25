from fastapi import FastAPI

from app.database import Base, engine
from app.routers import projects, reports, timelogs, users

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(users.router, prefix="/users")
app.include_router(projects.router, prefix="/projects")
app.include_router(timelogs.router, prefix="/timelogs")
app.include_router(reports.router, prefix="/reports")
