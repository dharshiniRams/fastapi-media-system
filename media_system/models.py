from sqlalchemy import Column, Integer, String, DateTime, func,ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class Customer(Base):
    
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    phone = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    media_items = relationship("Media", back_populates="customer")

class Media(Base):
    
    __tablename__="media"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    category = Column(String, index=True)
    author_or_artist = Column(String)
    store_name = Column(String, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    customer = relationship("Customer", back_populates="media_items")
