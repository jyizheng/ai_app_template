from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db import get_db

router=APIRouter()

@router.get("/")
def list_items(db: Session = Depends(get_db)):
    rows=db.execute("SELECT id, name FROM item LIMIT 10")
    return [dict(r) for r in rows]
