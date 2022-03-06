from sqlalchemy.orm import Session
from db.models import DbUser
from routes.schemas_user import UserBase,UserDisplay

def create_user(db:Session,request:UserBase):
    new_user = DbUser(
    company_id= request.company_id,
    organization_id= request.organization_id,
    current_organization_id= request.current_organization_id,
    user_name= request.user_name,
    user_position= request.user_position,
    user_email= request.user_email,
    user_password= request.user_password,
    user_available= request.user_available,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return create_user