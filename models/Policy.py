from pydantic import BaseModel
from datetime import date

class Policy(BaseModel):
    id: str
    account_id: str
    product: str
    startDate: date
    endDate: date
    provider: str
    premium: float
    notes: str

class Policy_List(BaseModel):
    totalSize: int
    records: list[Policy]