from fastapi import APIRouter

from models.Loan import LoanRequest, LoanResponse

loan_router = APIRouter()


def loan_calc(loan:float, rate:float):
    n =  12  # total number of months
    r = rate / (100 * 12)  # interest per month
    monthly_payment = loan * ((r * ((r + 1) ** n)) / (((r + 1) ** n) - 1))
    return monthly_payment
@loan_router.post("/loan")
def loan(loan_request: LoanRequest)->LoanResponse:

    monthlyPayment = loan_calc(loan_request.loan, loan_request.rate)
    totalPayment = monthlyPayment * 12

    lr = LoanResponse(monthly=monthlyPayment, total=totalPayment)

    return lr

