from fastapi import FastAPI, APIRouter, Depends
from .. import database, schemas
from . import service
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(prefix="/api", tags=["User"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
@router.post("/user")
def createUser(request: schemas.userType, db: Session = Depends(get_db)):
    return service.createUser(request, db)

@router.get("/user", response_model = List[schemas.userReponseType])
def get_users(db: Session = Depends(get_db)):
    return service.getUsers(db)
  
        
