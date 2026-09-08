from app.database.connection import SessionLocal
from app.schemas.common import StandardResponse
from fastapi import APIRouter,Depends
from app.schemas.transaction import TransactionResponse ,TransactionRequest
from sqlalchemy.orm import Session
from app.services.transaction import create_transactions,get_all_transactions,update_transaction
from typing import List


router=APIRouter()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/transactions",response_model=StandardResponse[TransactionResponse],status_code=201)
def add_transaction(transaction_data:TransactionRequest,db:Session=Depends(get_db)):
    transactions=create_transactions(transaction_data,db)
    return StandardResponse(status_code=201,status_message="Success",response_data=transactions)


@router.get("/transactions",response_model=StandardResponse[List[TransactionResponse]])
def get_transactions(transaction_id:int |None=None,db:Session=Depends(get_db)):
    transactions=get_all_transactions(transaction_id,db)
    return StandardResponse(status_code=200,status_message="Success",response_data=transactions)


@router.put("/transactions/{transaction_id}",response_model=StandardResponse[TransactionResponse])
def put_transaction(transaction_id:int,transaction_data:TransactionRequest,db:Session=Depends(get_db)):
    transactions=update_transaction(transaction_id,transaction_data,db)
    return StandardResponse(status_code=200,status_message="Success",response_data=transactions)
    