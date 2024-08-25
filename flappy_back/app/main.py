from fastapi import FastAPI
from .database import engine, Base
from .api import users, scores

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router, prefix="/api/v1", tags=["users"])
app.include_router(scores.router, prefix="/api/v1", tags=["scores"])

