from sqlalchemy import Column, Integer, String
from .base import Base

class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String,nullable=False)
    quantity = Column(Integer,default=0)