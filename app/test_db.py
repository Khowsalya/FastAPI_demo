from app.database import SessionLocal
from app.models.loan_model import Loan

db = SessionLocal()

try:
    # loan = Loan(
    #     applicant_name="Kumar",
    #     business_name="ABC Traders",
    #     loan_amount=500000,
    #     loan_status="PENDING"
    # )

    loans = [
    Loan(
        applicant_name="Ravi",
        business_name="Ravi Textiles",
        loan_amount=300000,
        loan_status="PENDING"
    ),
    Loan(
        applicant_name="Priya",
        business_name="Priya Boutique",
        loan_amount=750000,
        loan_status="PENDING"
    ),
    Loan(
        applicant_name="Arun",
        business_name="Arun Electronics",
        loan_amount=1000000,
        loan_status="PENDING"
    )
]

    db.add_all(loans)
    db.commit()

   
    for loan in loans:
        db.refresh(loan)

    print("Loan saved successfully!")
    for loan in loans:
        print("Loan ID:", loan.id)

except Exception as e:
    db.rollback()
    print("Error:", e)

finally:
    db.close()