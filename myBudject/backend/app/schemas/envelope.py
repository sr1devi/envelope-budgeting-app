from pydantic import BaseModel

class EnvelopeRequest(BaseModel):
    envelope_name:str

class EnvelopeResponse(BaseModel):
    envelope_name:int
    envelope_id:int


