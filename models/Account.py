from pydantic import BaseModel
from datetime import date

class Account(BaseModel):
    id: str
    email: str
    name: str
    dob: date
    addr1: str
    addr2: str
    city: str