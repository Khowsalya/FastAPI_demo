from sqlalchemy import select,or_
from app.database import SessionLocal
from app.models.loan_model import Loan

db = SessionLocal()

try:
    # statement = select(Loan).where(Loan.id == 1)
    # statement = select(Loan).where(Loan.applicant_name == "Kumar", Loan.loan_amount >= 400000)
    statement = select(Loan).where(or_(Loan.loan_status == "REJECTED", Loan.loan_amount < 400000))

    result = db.execute(statement)

    # loan = result.scalar_one_or_none()
    loan = result.scalars().all()

    if loan:
        for loan in loan:
            print("Loan ID:", loan.id)
            print("Applicant:", loan.applicant_name)
            print("Business:", loan.business_name)
            print("Amount:", loan.loan_amount)
            print("Status:", loan.loan_status)
    else:
        print("Loan not found")

finally:
    db.close()