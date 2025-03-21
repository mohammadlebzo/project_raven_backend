from sqlalchemy.orm import Session

from server.daos.item import get_item_dao, get_items_dao, get_items_count_dao
import server.schemas.item as schema

def get_item(db: Session, id: int):
    return get_item_dao(db, id)

def get_items(db: Session, page:int=0, size:int=100, locFilter:str=""):
    items = get_items_dao(db, page, size, locFilter)
    totla = get_items_count_dao(db, locFilter)
    return schema.ItemWithCount(
        items=items,
        full_total=totla
    )