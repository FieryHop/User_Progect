from datetime import date

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import func
from sqlalchemy.orm import Session

from app import models
from app.database import get_db

router = APIRouter()


@router.get("/reports/project/{project_id}")
def get_report(
    project_id: int,
    start_date: date = Query(..., description="Дата начала периода (включительно)"),
    end_date: date = Query(..., description="Дата окончания периода (не включительно)"),
    manager_id: int = Query(..., description="ID менеджера проекта"),
    db: Session = Depends(get_db),
):
    project = db.query(models.Project).filter(models.Project.id == project_id).first()
    if not project or project.manager_id != manager_id:
        raise HTTPException(status_code=403, detail="Доступ запрещен")

    report = (
        db.query(models.TimeLog.user_id, func.sum(models.TimeLog.hours).label("hours"))
        .filter(
            models.TimeLog.project_id == project_id,
            models.TimeLog.date_field >= start_date,
            models.TimeLog.date_field < end_date,
        )
        .group_by(models.TimeLog.user_id)
        .all()
    )

    return {"items": [{"id": user_id, "hours": hours} for user_id, hours in report]}
