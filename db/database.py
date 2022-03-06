from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,scoped_session
 
SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:1@localhost:3306/subtest?charset=utf8mb4'
 
engine = create_engine(SQLALCHEMY_DATABASE_URL,  pool_recycle=3600, pool_size=10, max_overflow=20, echo=False)
 
SessionLocal = scoped_session(sessionmaker(bind=engine, autocommit=True, autoflush=False))
 
Base = declarative_base()
 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()