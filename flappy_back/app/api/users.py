from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, models, database

router = APIRouter()


@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    db_user = crud.get_user_by_wallet(db, wallet_address=user.wallet_address)
    if db_user:
        raise HTTPException(status_code=400, detail="User already registered")
    return crud.create_user(db, user=user)


@router.get("/users/{wallet_address}", response_model=schemas.User)
def read_user(wallet_address: str, db: Session = Depends(database.get_db)):
    db_user = crud.get_user_by_wallet(db, wallet_address=wallet_address)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
