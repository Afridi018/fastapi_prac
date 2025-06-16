from .super_dao import SuperDao
from ..models import User
from sqlalchemy.orm import Session
from .. import schemas, models
from .. import hashing


class UserDao(SuperDao[User] ) :
    def __init__(self, db: Session):
        super().__init__(User, db)
        
        self.db = db
        
    def createUser(self, request: schemas.userType) ->  User:
        
        hashedpass = hashing.hash(request.password)
        newUser = models.User(email = request.email, password = hashedpass)
        
        self.db.add(newUser)
        self.db.commit()
        self.db.refresh(newUser)
        
        return newUser