from fastapi import FastAPI, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.routing import APIRoute
from models.Message import Message
from routers import query, policy, account, offers, loan

app = FastAPI()
app.include_router(query.query_router)
app.include_router(policy.policy_router)
app.include_router(account.account_router)
app.include_router(offers.offer_router)
app.include_router(loan.loan_router)

security = HTTPBasic()


@app.get("/ping",
         summary='Ping',
         description='Ping',
         )
def ping(credentials: HTTPBasicCredentials = Depends(security)) -> Message:

    m = Message(message="WxO L3 V2 services are alive")
    return m




def use_route_names_as_operation_ids(app: FastAPI) -> None:
    """
    Simplify operation IDs so that generated API clients have simpler function
    names.

    Should be called only after all routes have been added.
    """
    for route in app.routes:
        if isinstance(route, APIRoute):
            route.operation_id = route.name  # in this case, operation ID will be 'greeting'


use_route_names_as_operation_ids(app)