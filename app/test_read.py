from sqlalchemy import select
from app.database import SessionLocal
from app.models.loan_model import Loan

db = SessionLocal()

try:
    statement = select(Loan)

    result = db.execute(statement)

    loans = result.scalars().all()

    for loan in loans:
        print(loan.id)
        print(loan.applicant_name)
        print(loan.business_name)
        print(loan.loan_amount)
        print(loan.loan_status)
        print("------------------")

finally:
    db.close()