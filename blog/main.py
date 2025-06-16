from fastapi import FastAPI, Depends, File, UploadFile
from . import models, schemas


from .database import engine, SessionLocal, Base

from sqlalchemy.orm import Session

from . import hashing


from blog.users.routes import router as user_router


from fastapi.staticfiles import StaticFiles
import os, shutil



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





UPLOAD_DIR = "uploaded_images"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Mount the static directory to serve images via URL
app.mount("/images", StaticFiles(directory=UPLOAD_DIR), name="images")

@app.post("/upload-image/")
async def upload_image(image: UploadFile = File(...)):
    if not image.content_type.startswith("image/"):
        return {"error": "File is not an image."}

    file_path = os.path.join(UPLOAD_DIR, image.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    image_url = f"/images/{image.filename}"
    return {"filename": image.filename, "url": f"http://127.0.0.1:8000{image_url}"}