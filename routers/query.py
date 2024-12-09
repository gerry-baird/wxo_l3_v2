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
async def customers_with_life_events(q: str="q=select+Id,AccountId,Name,Email,Recent_Change__c,Child_Age__c,Child_Covered__c,Child_Name__c+from+contact+where+AccountId='001Hs00002ubq6YIAQ'") -> Customer_List:
    customer_list = create_customers()
    return customer_list

