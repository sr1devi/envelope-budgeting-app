from typing import Generic,TypeVar
from pydantic import BaseModel
T=TypeVar("T")

class StandardResponse(BaseModel,Generic[T]):
    status_code:int
    status_message:str
    error_message:str |None=None
    response_data:T
