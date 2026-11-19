from typing import Any

from pydantic import BaseModel, Field, field_validator

class LoanRequest(BaseModel):
    applicant_id:int = Field(gt=0, description="The ID of the applicant")
    business_name:str = Field(min_length=3, max_length=100, description="The name of the business")
    annual_turnover:float = Field(ge=0, description="The annual turnover of the business")
    loan_amount:float= Field(gt=0, description="The requested loan amount")

    @field_validator("business_name", mode="before")
    @classmethod
    def validate_business_name(cls, value: Any) -> Any:
        print("Received:", repr(value))
        if isinstance(value, str) and not value.strip():
            raise ValueError("Business name cannot be empty")
        return value
