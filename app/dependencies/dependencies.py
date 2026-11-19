from fastapi import Request
from app.database import SessionLocal

def get_api_version(request:Request):
    parts= request.url.path.strip("/").split("/")
    if len(parts)>=2 and parts[0]=='api':
        return parts[1]


def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

     