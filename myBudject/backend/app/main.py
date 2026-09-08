from fastapi import FastAPI
from app.database.connection import Base,engine
from app.models.user import User
from app.models.envelope import Envelope
from app.models.transaction import Transaction

Base.metadata.create_all(bind=engine)
app=FastAPI()

@app.get("/")
def home():
    return{"message":"Budget API is running"}
