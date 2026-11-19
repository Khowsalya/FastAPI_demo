from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Loan(Base):
    __tablename__ = "loans"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    applicant_id: Mapped[int] = mapped_column(Integer, nullable=False)

    business_name: Mapped[str] = mapped_column(String(150), nullable=False)

    annual_turnover: Mapped[float] = mapped_column(Float, nullable=False)

    loan_amount: Mapped[float] = mapped_column(Float, nullable=False)

    loan_status: Mapped[str] = mapped_column(String(50), default="PENDING")

    reason: Mapped[str] = mapped_column(String(255), nullable=True)