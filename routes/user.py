from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from db.db_user import create_user
from routes.schemas_user import UserBase, UserDisplay
router = APIRouter(
    prefix='/user',
    tags=['user']
)

@router.post('/user',response_model=UserDisplay)
def create_user(request:UserBase,db:Session=Depends(get_db)):
    return create_user(db,request)
