from sqlalchemy import Column, DateTime, ForeignKey, Integer,String,func
from app.database.connection import Base
class Token(Base):
    __tablename__="token"
    token_id=Column(Integer,primary_key=True)
    user_id=Column(Integer,ForeignKey("user.user_id"))
    token_hash=Column(String(100),nullable=False)
    issued_at=Column(DateTime(timezone=True),nullable=False,server_default=func.now())
    expires_at=Column(DateTime(timezone=True),nullable=False)
    revoked_at=Column(DateTime(timezone=True),nullable=True)
__all__=["Token"]