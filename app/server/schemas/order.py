from datetime import datetime

from pydantic import BaseModel

class OrderBase(BaseModel):
    class Config:
        orm_mode = True

class Order(OrderBase):
    id : int
    item_id: int
    created_at: datetime
