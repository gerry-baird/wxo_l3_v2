from pydantic import BaseModel

class Customer(BaseModel):
    name: str
    age: int
    id: str
    email: str
    recent_change: str

class Customer_List(BaseModel):
    totalSize: int
    records: list[Customer]