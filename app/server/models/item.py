from sqlalchemy import Column, Integer, String, Double

from server.config.database import Base

class Item(Base):
    __tablename__ = "items"
    
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String(255),index=True)
    description = Column(String(255), index=True)
    price = Column(Double, index=True)
    location = Column(String(10), index=True)
