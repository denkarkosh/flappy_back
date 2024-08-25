from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    wallet_address = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    nft_minted = Column(Integer, default=0)
    scores = relationship("Score", back_populates="owner")


class Score(Base):
    __tablename__ = 'scores'

    id = Column(Integer, primary_key=True, index=True)
    value = Column(Float, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship("User", back_populates="scores")
