from sqlalchemy.orm import Session
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