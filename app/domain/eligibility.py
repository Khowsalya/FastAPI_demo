def check_eligibility(annual_turnover: float, loan_amount: float):
    if annual_turnover <= 0:
        return {
            "status": "manual_review",
            "reason": "Business turnover must be positive"
        }

    if loan_amount > annual_turnover:
        return {
            "status": "manual_review",
            "reason": "Loan amount exceeds annual turnover"
        }

    return {
        "status": "eligible_for_review",
        "reason": "Initial business rule passed"
    }