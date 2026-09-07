from app.database.connection import Base
from sqlalchemy import Column,String,ForeignKey,Integer,DateTime
from datetime import datetime

class Transcation(Base):
    __tablename__="transaction"
    transaction_id=Column(Integer,primary_key=True)
    envolepe_id=Column(Integer,ForeignKey("envolepe.envolepe_id"))
    user_id=Column(Integer,ForeignKey("user.user_id"))
    