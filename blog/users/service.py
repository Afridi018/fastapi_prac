from sqlalchemy.orm import Session
from .. import schemas, models
from .. import hashing
from ..daos.user_dao import UserDao

def createUser(request: schemas.userType, db: Session ):
    return UserDao(db).createUser(request)


def getUsers(db: Session):
    return UserDao(db).get_all()
     