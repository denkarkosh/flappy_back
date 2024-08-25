from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter()


@router.post("/users/{user_id}/scores/", response_model=schemas.Score)
def create_score_for_user(user_id: int, score: schemas.ScoreCreate, db: Session = Depends(database.get_db)):
    return crud.create_user_score(db, score=score, user_id=user_id)


@router.get("/users/{user_id}/scores/", response_model=List[schemas.Score])
def read_user_scores(user_id: int, db: Session = Depends(database.get_db)):
    return crud.get_user_scores(db, user_id=user_id)


@router.get("/leaderboard/", response_model=List[schemas.Score])
def get_leaderboard(db: Session = Depends(database.get_db), limit: int = 10):
    return crud.get_leaderboard(db, limit=limit)
