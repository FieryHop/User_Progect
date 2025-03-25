from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import get_db

router = APIRouter()


@router.post("/", response_model=schemas.TimeLog)
def create_timelog(timelog: schemas.TimeLogCreate, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == timelog.user_id).first()
    project = (
        db.query(models.Project).filter(models.Project.id == timelog.project_id).first()
    )

    if not user:
        raise HTTPException(status_code=400, detail="Пользователь не найден")
    if not project:
        raise HTTPException(status_code=400, detail="Проект не найден")

    db_timelog = models.TimeLog(**timelog.model_dump())
    db.add(db_timelog)
    db.commit()
    db.refresh(db_timelog)
    return db_timelog


@router.get("/", response_model=List[schemas.TimeLog])
def get_all_timelogs(db: Session = Depends(get_db)):
    return db.query(models.TimeLog).all()


@router.get("/{timelog_id}", response_model=schemas.TimeLog)
def get_timelog(timelog_id: int, db: Session = Depends(get_db)):
    timelog = db.query(models.TimeLog).filter(models.TimeLog.id == timelog_id).first()
    if not timelog:
        raise HTTPException(status_code=404, detail="Запись времени не найдена")
    return timelog


@router.put("/{timelog_id}", response_model=schemas.TimeLog)
def update_timelog(
    timelog_id: int, timelog_data: schemas.TimeLogUpdate, db: Session = Depends(get_db)
):
    timelog = db.query(models.TimeLog).filter(models.TimeLog.id == timelog_id).first()
    if not timelog:
        raise HTTPException(status_code=404, detail="Запись времени не найдена")

    for key, value in timelog_data.model_dump(exclude_unset=True).items():
        setattr(timelog, key, value)

    db.commit()
    db.refresh(timelog)
    return timelog


@router.delete("/{timelog_id}")
def delete_timelog(timelog_id: int, db: Session = Depends(get_db)):
    timelog = db.query(models.TimeLog).filter(models.TimeLog.id == timelog_id).first()
    if not timelog:
        raise HTTPException(status_code=404, detail="Запись времени не найдена")

    db.delete(timelog)
    db.commit()
    return {"message": "Запись времени удалена"}
