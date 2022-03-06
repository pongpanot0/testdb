from .database import Base
from sqlalchemy.dialects.mysql import VARCHAR,TINYINT,TEXT
from sqlalchemy import Column,Integer,String,DateTime,Text, false

class DbUser(Base):
    __tablename__ = 'users'
    user_id = Column(Integer,primary_key=True,index=True)
    company_id = Column(Integer,nullable=false)
    organization_id = Column(Integer,nullable=false)
    current_organization_id = Column(Integer,nullable=false)
    user_name = Column(VARCHAR(100))
    user_position = Column(VARCHAR(100))
    user_email = Column(VARCHAR(100),nullable=false)
    user_password = Column(TEXT(100),nullable=false)
    user_available = Column(TINYINT(1),nullable=false,default=1)
    activate_at = Column(DateTime)
    language_id = Column(Integer,nullable=false)
    theme_id = Column(Integer,nullable=false)
    created_at = Column(DateTime)
    created_by = Column(Integer)
    updated_at = Column(DateTime)
    updated_by = Column(Integer)
    in_active = Column(TINYINT(1),default=0)
    
    
class Dborganiaztion(Base):
    __tablename__ = 'organiaztion'
    organiaztion_id = Column(Integer,primary_key=True,index=True)
    company_id = Column(Integer)
    organization_name = Column(VARCHAR(50))
    organization_parent = Column(Integer)
    langauage_id = Column(Integer)
    theme_id = Column(Integer)
    create_at = Column(DateTime)
    created_by = Column(Integer) #ดึงมาจาก USER ID
    updated_at = Column(DateTime)
    updated_by = Column(Integer) #ดึงมาจาก USER ID
    in_active = Column(TINYINT(1),default=0)