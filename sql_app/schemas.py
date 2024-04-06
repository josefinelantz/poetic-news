from pydantic import BaseModel 

class ArticleBase(BaseModel):
  title: str
  text: str
  poetry: str | None = None
  
class ArticleCreate(ArticleBase):
  pass 

class Article(ArticleBase):
  id: int 
  class Config:
    from_attributes = True 