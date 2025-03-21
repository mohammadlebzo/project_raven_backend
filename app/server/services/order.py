from sqlalchemy.orm import Session

from server.daos.order import make_order_dao
from server.daos.item import get_item_dao

def make_order(db: Session, id: int):
    order = make_order_dao(db, id)
    return get_item_dao(db, order.item_id)
