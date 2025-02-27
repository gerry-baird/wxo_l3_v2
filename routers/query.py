from fastapi import APIRouter
from data.customer_data import create_customers
from models.Customer import Customer_List

query_router = APIRouter()

@query_router.get("/query",
         summary='Get a list of customers with recent life events',
         description='Get a list of customers with recent life events',
         response_description="Customers with recent life events",
         tags=["Customers"]
         )
def customers_with_life_events(q: str="not used") -> Customer_List:
    customer_list = create_customers()
    return customer_list

