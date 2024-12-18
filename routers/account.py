from fastapi import APIRouter, HTTPException
from starlette import status

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
    raise HTTPException(status_code=404, detail='Account not found')