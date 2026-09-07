
from app.database.connection import Base
from sqlalchemy import Column, ForeignKey,String,Integer

class Envelope(Base):
    __tablename__="envelope"
    envelope_id=Column(Integer,primary_key=True)
    envelope_name=Column(String(50),nullable=False)
    budget_amount=Column(Integer,nullable=False)
    available_amount=Column(Integer,nullable=False)
    user_id=Column(Integer,ForeignKey("user.user_id"))
    alert_threshold=Column(Integer,nullable=True)
    