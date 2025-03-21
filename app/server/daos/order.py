from sqlalchemy.orm import Session

from server.models.order import Order

def make_order_dao(db: Session, item_id:int):
    order = Order(item_id=item_id)
    db.add(order)
    db.commit()
    db.refresh(order)
    return order

