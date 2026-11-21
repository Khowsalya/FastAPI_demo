from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schema.loan_schema import LoanRequest,LoanUpdateRequest,LoanPartialUpdateRequest
from app.service.loan_service import process_loan,fetch_all_loans,fetch_loan_by_id,update_loan,patch_loan
from app.dependencies.dependencies import get_api_version,get_db


router = APIRouter(prefix="/loans",tags=["loans"])


@router.post("/")
def create_loan(loan_request:LoanRequest,db: Session=Depends(get_db),api_version:str=Depends(get_api_version)):
    result= process_loan(loan_request,db)

    return {
        "api_version":api_version,
        "loan_data":result
    }

@router.get("/")
def get_all_loan_details(
    db: Session = Depends(get_db),
    api_version: str = Depends(get_api_version)
):
    loans = fetch_all_loans(db)

    return {
        "api_version": api_version,
        "total_loans": len(loans),
        "loans": loans
    }

@router.get("/{loan_id}")
def get_loan_details(
    loan_id: int,
    db: Session = Depends(get_db),
    api_version: str = Depends(get_api_version)
):
    loan = fetch_loan_by_id(db, loan_id)

    if loan is None:
        raise HTTPException(
            status_code=404,
            detail=f"Loan with ID {loan_id} not found"
        )

    return {
        "api_version": api_version,
        "loan": loan
    }


@router.put("/{loan_id}")
def update_loan_details(
    loan_id: int,
    loan_request: LoanUpdateRequest,
    db: Session = Depends(get_db),
    api_version: str = Depends(get_api_version)
):
    loan = update_loan(
        db,
        loan_id,
        loan_request.model_dump()
    )

    if loan is None:
        raise HTTPException(
            status_code=404,
            detail=f"Loan with ID {loan_id} not found"
        )

    return {
        "api_version": api_version,
        "message": "Loan updated successfully",
        "loan": loan
    }

@router.put("/{loan_id}")
def update_loan_details(
    loan_id: int,
    loan_request: LoanUpdateRequest,
    db: Session = Depends(get_db),
    api_version: str = Depends(get_api_version)
):
    loan = update_loan(
        db,
        loan_id,
        loan_request.model_dump()
    )

    if loan is None:
        raise HTTPException(
            status_code=404,
            detail=f"Loan with ID {loan_id} not found"
        )

    return {
        "api_version": api_version,
        "message": "Loan updated successfully",
        "loan": loan
    }


@router.patch("/{loan_id}")
def patch_loan_details(
    loan_id: int,
    loan_request: LoanPartialUpdateRequest,
    db: Session = Depends(get_db),
    api_version: str = Depends(get_api_version)
):
    update_data = loan_request.model_dump(
        exclude_unset=True,
        exclude_none=True
    )

    if not update_data:
        raise HTTPException(
            status_code=400,
            detail="No fields provided for update"
        )

    loan = patch_loan(db, loan_id, update_data)

    if loan is None:
        raise HTTPException(
            status_code=404,
            detail=f"Loan with ID {loan_id} not found"
        )

    return {
        "api_version": api_version,
        "message": "Loan updated successfully",
        "loan": loan
    }