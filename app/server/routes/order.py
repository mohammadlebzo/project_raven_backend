from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from server.config.database import engine, get_db
import server.models.order as model
import server.schemas.item as schema
from server.services.order import make_order

model.Base.metadata.create_all(bind=engine)

router = APIRouter()

@router.post("/{purchase_id}", response_model=schema.Item)
def post_user(purchase_id:int, db:Session=Depends(get_db)):
    return make_order(db, purchase_id)
