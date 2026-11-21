from typing import Any
from sqlalchemy.orm import Session
from app.models.loan_model import Loan
from app.schema.loan_schema import LoanRequest
from app.domain.eligibility import check_eligibility
from app.repoistories.loan_respoistories import save_loan,get_all_loans,get_loan_by_id


def process_loan(loan_request:LoanRequest,db:Session)->dict:
    eligibility_result = check_eligibility(loan_request.annual_turnover, loan_request.loan_amount)
    loan_data= {
        "applicant_id":loan_request.applicant_id,
        "business_name":loan_request.business_name,
        "annual_turnover":loan_request.annual_turnover,
        "loan_amount": loan_request.loan_amount,
        "loan_status":eligibility_result["status"],
        "reason":eligibility_result["reason"]
    }

    save_data = save_loan(loan_data,db)

    return save_data

def fetch_all_loans(db: Session):
    loans = get_all_loans(db)
    return loans

def fetch_loan_by_id(db: Session, loan_id: int):
    loan = get_loan_by_id(db, loan_id)
    return loan

def update_loan(db: Session, loan_id: int, loan_data: dict):
    loan = db.get(Loan, loan_id)

    if loan is None:
        return None

    loan.business_name = loan_data["business_name"]
    loan.annual_turnover = loan_data["annual_turnover"]
    loan.loan_amount = loan_data["loan_amount"]

    db.commit()
    db.refresh(loan)

    return loan

def patch_loan(db: Any, loan_id: int, loan_data: dict):
    loan = db.get(Loan, loan_id)

    if loan is None:
        return None

    for field, value in loan_data.items():
        setattr(loan, field, value)

    db.commit()
    db.refresh(loan)

    return loan