from fastapi import FastAPI, Depends
from . import models, schemas


from .database import engine, SessionLocal, Base

from sqlalchemy.orm import Session

from . import hashing


from blog.users.routes import router as user_router



models.Base.metadata.create_all(bind=engine)


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

# @app.post("/")
# def createBlog(request: schemas.blogType):
# return request




@app.post("/blog",summary="List all upload processes",
    description="List all video upload processes with pagination")
def createBlog(request: schemas.blogType, db: Session = Depends(get_db)):
    newBlog = models.Item(title = request.title, description = request.description )
    print(newBlog)
    db.add(newBlog)
    db.commit()
    db.refresh(newBlog)
    print(newBlog)
    return newBlog

@app.get("/blog")
def get_blog(db: Session = Depends(get_db)):
    blogs = db.query(models.Item).all()
    return blogs

@app.get("/blog/{id}")
def get_single(id, db: Session = Depends(get_db)):
    blog = db.query(models.Item).filter(models.Item.id == id).first()
    return blog
    
    
# @app.post("/user")
# def createUser(request: schemas.userType, db: Session = Depends(get_db)):
    
#     hashedPass = hashing.hash(request.password)
    
#     newUser = models.User(email = request.email, password = hashedPass )
    
#     db.add(newUser)
#     db.commit()
#     db.refresh(newUser)
    
#     return newUser
    

app.include_router(user_router)    
    
    
@app.get("/")
def test():
    return "hello world"