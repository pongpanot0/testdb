from datetime import datetime
from pydantic import BaseModel

class UserBase(BaseModel):
    company_id:int
    organization_id:int
    current_organization_id:int
    user_name:str
    user_position:str
    user_email:str
    user_password:str
    user_available:int
    
class UserDisplay(BaseModel):
    company_id:int
    organization_id:int
    current_organization_id:int
    user_name:str
    user_position:str
    user_email:str
    user_password:str
    user_available:int
    class config():
        orm_mode = True