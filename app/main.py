from fastapi import FastAPI
from app.routers.loan_routes import router as loan_router

app=FastAPI(title="MSME Loan API")

app.include_router(loan_router,prefix="/api/v1")

@app.get("/")
def home():
    return {"message": "MSME Loan API is running successfully!"}    