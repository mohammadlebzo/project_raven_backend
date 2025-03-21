from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from server.config.database import engine, get_db
import server.models.item as model
import server.schemas.item as schema
from server.services.item import get_item, get_items

model.Base.metadata.create_all(bind=engine)

router = APIRouter()

@router.get("/{id}/",response_model=schema.Item)
def get_user(id:int, db:Session=Depends(get_db)):
    db_user = get_item(db, id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_user

@router.get("/", response_model=schema.ItemWithCount)
def get_users(page_number:int=0, page_size:int=0, location:str="",db:Session=Depends(get_db)):
    return get_items(db, page_number, page_size, location)