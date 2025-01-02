from fastapi import APIRouter, HTTPException
from starlette import status
from datetime import date
from data.account_data import create_accounts
from models.Account import Account

account_router = APIRouter()

@account_router.get("/account", status_code=status.HTTP_200_OK,
         summary='Get the details of an account',
         description='Get the details of an account',
         response_description="Account details",
         tags=["Account"]
         )
async def get_account(account_id: str) -> Account:
    account_list = create_accounts()

    for acc in account_list:
        if acc.id == account_id:
            return acc

    # if account not found return empty Account record
    unknown_account = Account(
        id=account_id,
        email="Not found",
        name="Not found",
        dob=date(1900, 1, 1),
        addr1="Not found",
        addr2="Not found",
        city="Not found"
    )
    return unknown_account