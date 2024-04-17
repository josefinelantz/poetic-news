from typing import Union
from fastapi import Depends, FastAPI, HTTPException 
from sqlalchemy.orm import Session 
from . import crud, models, schemas 
from .database import SessionLocal, engine 

models.Base.metadata.create_all(bind=engine)

app = FastAPI() 

# Dependency
def get_db():
  db = SessionLocal() 
  try: 
    yield db 
  finally: 
    db.close() 
    
@app.get("/")
async def root():
  return {"message": "Hello World"}
    
@app.post("/articles/", response_model=schemas.Article)
async def create_article(article: schemas.ArticleCreate, db: Session = Depends(get_db)):
  db_article = crud.get_article_by_title(db, title=article.title)
  if db_article:
    raise HTTPException(status_code=400, detail="Article already registered")
  return crud.create_article(db=db, article=article)

@app.get("/articles", response_model=list[schemas.Article])
async def read_articles(skip: int = 0, limit: int= 100, db: Session = Depends(get_db)):
  articles = crud.get_articles(db, skip=skip, limit=limit)
  return articles 
  