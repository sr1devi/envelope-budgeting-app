from app.database.connection import SessionLocal
from app.schemas.common import StandardResponse
from fastapi import APIRouter,Depends
from app.schemas.envelope import EnvelopeResponse ,EnvelopeRequest
from sqlalchemy.orm import Session
from app.services.envelope import create_envelope,get_all_envelopes,update_envelope
from typing import List


router=APIRouter()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/envelopes",response_model=StandardResponse[EnvelopeResponse],status_code=201)
def add_transaction(envelope_data:EnvelopeRequest,db:Session=Depends(get_db)):
    envelopes=create_envelope(envelope_data,db)
    return StandardResponse(status_code=201,status_message="Success",response_data=envelopes)


@router.get("/envelopes",response_model=StandardResponse[List[EnvelopeResponse]])
def get_envelopes(envelope_id:int |None=None,db:Session=Depends(get_db)):
    envelopes=get_all_envelopes(envelope_id,db)
    return StandardResponse(status_code=200,status_message="Success",response_data=envelopes)


@router.put("/envelope/{envelope_id}",response_model=StandardResponse[EnvelopeResponse])
def put_envelope(envelope_id:int,envelope_data:EnvelopeRequest,db:Session=Depends(get_db)):
    transactions=update_envelope(envelope_id,envelope_data,db)
    return StandardResponse(status_code=200,status_message="Success",response_data=envelopes)
    