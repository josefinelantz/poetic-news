from pydantic import BaseModel 

class ArticleBase(BaseModel):
  title: str
  published: str 
  url: str 
  text: str 
  poetry: str
  
class ArticleCreate(ArticleBase):
  pass 

class Article(ArticleBase):
  id: int 
  class Config:
    from_attributes = True 