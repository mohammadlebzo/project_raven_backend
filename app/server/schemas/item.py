from pydantic import BaseModel

class ItemBase(BaseModel):
    class Config:
        orm_mode = True

class Item(ItemBase):
    id : int
    title: str
    description: str
    price: float
    location: str

class ItemWithCount(ItemBase):
    items: list[Item]
    full_total: int

