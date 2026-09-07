from sqlalchemy import Column,Integer,String,DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime
from app.database.connection import Base

class User(Base):
    __tablename__="user"
    user_id=Column(Integer,primary_key=True)
    username=Column(String(50),unique=True,nullable=False)
    password=Column(String(100),nullable=False)
    created_at=Column(DateTime,default=datetime.now)
__all__=["User"]