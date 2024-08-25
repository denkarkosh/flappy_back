from pydantic import BaseModel
from typing import List, Optional


class ScoreBase(BaseModel):
    value: float


class ScoreCreate(ScoreBase):
    pass


class Score(ScoreBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str
    wallet_address: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    nft_minted: int
    scores: List[Score] = []

    class Config:
        orm_mode = True
