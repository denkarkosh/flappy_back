from sqlalchemy.orm import Session
from . import models, schemas


def get_user_by_wallet(db: Session, wallet_address: str):
    return db.query(models.User).filter(models.User.wallet_address == wallet_address).first()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(username=user.username, wallet_address=user.wallet_address)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_user_score(db: Session, score: schemas.ScoreCreate, user_id: int):
    db_score = models.Score(**score.dict(), user_id=user_id)
    db.add(db_score)
    db.commit()
    db.refresh(db_score)
    return db_score


def get_user_scores(db: Session, user_id: int):
    return db.query(models.Score).filter(models.Score.user_id == user_id).all()


def get_leaderboard(db: Session, limit: int = 10):
    return db.query(models.Score).order_by(models.Score.value.desc()).limit(limit).all()
