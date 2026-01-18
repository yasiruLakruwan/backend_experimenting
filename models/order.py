from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship
from db.base import Base

class order(Base):
    __tablename__="orders"

    # id = Column(I)