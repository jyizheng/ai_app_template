from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from common.config import SUPABASE_DB_URL

engine=create_engine(SUPABASE_DB_URL)
SessionLocal=sessionmaker(bind=engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
