from datetime import datetime, timezone

from sqlalchemy import Column, Integer, DateTime

from server.config.database import Base

class Order(Base):
    __tablename__ = "orders"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement="auto")
    item_id = Column(Integer, index=True)
    created_at = Column(DateTime, index=True, default=datetime.now(timezone.utc))
