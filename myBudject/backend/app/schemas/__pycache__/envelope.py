from pydantic import BaseModel
from datetime import datetime

class EnvelopeRequest(BaseModel):
    envelope_name:str
    envelope_amount:int
    envelope_date:datetime