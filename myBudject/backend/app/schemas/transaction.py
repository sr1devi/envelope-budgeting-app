from pydantic import BaseModel
from datetime import datetime

class TransactionRequest(BaseModel):
    envelope_id:int
    user_id:int
    available_amount:int
    transaction_amount:int
    transaction_date:datetime

class TransactionResponse(BaseModel):
    transaction_id:int
    transaction_amount:int
    available_amount:int
