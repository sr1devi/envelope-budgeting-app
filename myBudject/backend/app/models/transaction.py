from app.database.connection import Base
from sqlalchemy import Column,String,ForeignKey,Integer,DateTime
from datetime import datetime
import uuid
from sqlalchemy.dialects.postgresql import UUID

class Transaction(Base):
    __tablename__="transaction"
    transaction_id=Column(UUID(as_uuid=True),default=uuid.uuid4,primary_key=True)
    envelope_id=Column(Integer,ForeignKey("envelope.envelope_id"))
    user_id=Column(Integer,ForeignKey("user.user_id"))
    available_amount=Column(Integer,nullable=False)
    transaction_amount=Column(Integer,nullable=False)
    transaction_date=Column(DateTime,default=datetime.utcnow)
__all__=["Transaction"]