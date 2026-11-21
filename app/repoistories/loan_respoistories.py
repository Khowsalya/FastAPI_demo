from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.loan_model import Loan


def save_loan(loan_data: dict, db: Session) -> dict:

    try:
        loan = Loan(**loan_data)

        db.add(loan)
        db.commit()
        db.refresh(loan)

        return {
            "message": "Loan data saved successfully",
            "loan_data": {
                "loan_id": loan.id,
                "applicant_id": loan.applicant_id,
                "business_name": loan.business_name,
                "annual_turnover": loan.annual_turnover,
                "loan_amount": loan.loan_amount,
                "loan_status": loan.loan_status,
                "reason": loan.reason
            }
        }

    except Exception as e:
        db.rollback()
        raise e

def get_all_loans(db: Session):
    statement = select(Loan)

    result = db.execute(statement)

    loans = result.scalars().all()

    return loans

def get_loan_by_id(db: Session, loan_id: int):
    statement = select(Loan).where(Loan.id == loan_id)

    result = db.execute(statement)

    loan = result.scalar_one_or_none()

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

def patch_loan(db: Session, loan_id: int, loan_data: dict):
    loan = db.get(Loan, loan_id)

    if loan is None:
        return None

    for field, value in loan_data.items():
        setattr(loan, field, value)

    db.commit()
    db.refresh(loan)

    return loan