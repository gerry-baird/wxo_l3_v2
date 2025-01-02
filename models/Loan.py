from pydantic import BaseModel
class CreditRequest(BaseModel):
    credit: float
    rate: float

class CreditResponse(BaseModel):
    monthly: float
    total: float