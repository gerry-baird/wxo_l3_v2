from pydantic import BaseModel
class LoanRequest(BaseModel):
    loan: float
    rate: float

class LoanResponse(BaseModel):
    monthly: float
    total: float