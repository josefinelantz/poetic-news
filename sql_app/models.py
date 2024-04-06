from sqlalchemy import Column, Integer, String 
from .database import Base 

class Article(Base):
  __tablename__ = "articles"
  
  id = Column(Integer, primary_key=True)
  title = Column(String, unique=True, index=True)
  text = Column(String, unique=True, index=True)
  poetry = Column(String, unique=True, index=True)
  