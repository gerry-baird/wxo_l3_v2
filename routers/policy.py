from fastapi import APIRouter, HTTPException
from starlette import status
import json
from data.policy_data import create_policies
from models.Policy import Policy, Policy_List, Policy_Summary

policy_router = APIRouter()

@policy_router.get("/policy/{policy_id}", status_code=status.HTTP_200_OK,
         summary='Get the details of a policy',
         description='Get the details of a policy',
         response_description="Policy details",
         tags=["Policy"]
         )
async def get_policy(policy_id: str) -> Policy:
    policy_list = create_policies()

    for p in policy_list.records:
        if p.id == policy_id:
            return p
    raise HTTPException(status_code=404, detail='Item not found')

@policy_router.get("/account/{account_id}/policies", status_code=status.HTTP_200_OK,
         summary='Get policies for a specific account',
         description='Get policies for a specific account',
         response_description="Account policies",
         tags=["Policy"]
         )
async def find_account_policy(account_id: str) -> Policy_List:
    policy_list = create_policies()

    results = list()
    for p in policy_list:
        if p.account_id == account_id:
            id = p.id
            startDate = p.startDate
            status = p.status
            product = p.product
            summary = Policy_Summary(id=id, startDate=startDate, status=status, product=product)
            results.append(summary)

    result_count = len(results)

    result_list = Policy_List(
        totalSize=result_count,
        records=results
    )

    if result_count > 0:
        print("Response data")
        print(result_list.model_dump())

        return result_list
    else:
        raise HTTPException(status_code=404, detail='Item not found')

