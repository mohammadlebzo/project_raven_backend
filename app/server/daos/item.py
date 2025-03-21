from sqlalchemy.orm import Session

from server.models.item import Item

def get_item_dao(db: Session, id: int):
    return db.query(Item).filter(Item.id == id).first()

def get_items_dao(db: Session, page:int=0, size:int=10, locFilter:str=""):
    if locFilter != "":
        return db.query(Item).filter(Item.location == locFilter.upper()).offset(( ( page - 1 ) * size ) if page > 0 else 0).limit(size).all()
    
    return db.query(Item).offset(( ( page - 1 ) * size ) if page > 0 else 0).limit(size).all()
