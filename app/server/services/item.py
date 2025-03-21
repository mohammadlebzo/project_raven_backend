from sqlalchemy.orm import Session

from server.daos.item import get_item_dao, get_items_dao

def get_item(db: Session, id: int):
    return get_item_dao(db, id)

def get_items(db: Session, page:int=0, size:int=100, locFilter:str=""):
    return get_items_dao(db, page, size, locFilter)