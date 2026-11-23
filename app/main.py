from fastapi import FastAPI, Request
from fastapi.exceptions import HTTPException, RequestValidationError
from fastapi.responses import JSONResponse
from app.routers.loan_routes import router as loan_router
import logging

app=FastAPI(title="MSME Loan API")
logger = logging.getLogger(__name__)

app.include_router(loan_router,prefix="/api/v1")

@app.get("/")
def home():
    return {"message": "MSME Loan API is running successfully!"}   

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "code": exc.status_code,
                "message": exc.detail
            }
        },
        headers=exc.headers
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):

    errors = []

    for error in exc.errors():
        errors.append({
            "field": ".".join(str(item) for item in error["loc"]),
            "message": error["msg"],
            "type": error["type"]
        })
    return JSONResponse(
        status_code=422,
        content={
            "error": {
                "code": 422,
                "message": "Validation failed",
                "details": errors
            }
        }
    ) 

@app.exception_handler(Exception)
async def global_exception_handler(
    request: Request,
    exc: Exception
):

    logger.exception("Unexpected error occurred")

    return JSONResponse(
        status_code=500,
        content={
            "error": {
                "code": 500,
                "message": "Internal server error"
            }
        }
    )


# Test case for 500 error code
# @app.get("/test-error")
# def test_error():
#     result = 10 / 0
#     return {"result": result}