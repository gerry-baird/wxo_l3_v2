from fastapi import APIRouter

from models.Loan import CreditRequest, CreditResponse

loan_router = APIRouter()


def loan_calc(credit:float, rate:float):
    n =  12  # total number of months
    r = rate / (100 * 12)  # interest per month
    monthly_payment = credit * ((r * ((r + 1) ** n)) / (((r + 1) ** n) - 1))
    return monthly_payment
@loan_router.post("/credit")
def loan(credit_request: CreditRequest)->CreditResponse:

    monthlyPayment = loan_calc(credit_request.credit, credit_request.rate)
    totalPayment = monthlyPayment * 12

    lr = CreditResponse(monthly=round(monthlyPayment,2), total=round(totalPayment,2))

    return lr

