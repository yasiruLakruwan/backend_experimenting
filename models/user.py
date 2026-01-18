from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship
from db.base import Base

class User(Base):
    __tablename__="users"

    id = Column(Integer,primary_key=True)
    email = Column(String,unique=True,index=True)
    hashed_passward = Column(String)

    orders = relationship("Order", back_populates="user")