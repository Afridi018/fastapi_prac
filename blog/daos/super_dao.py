from sqlalchemy.orm import Session
from typing import TypeVar, Generic, Type, List, Optional


ModelType = TypeVar("ModelType")

class SuperDao (Generic[ModelType]):
        def __init__(self, model: Type[ModelType], db: Session):
            self.model = model
            self.db = db
        
        def get_all (self) -> List[ModelType] :
            return self.db.query(self.model).all() 
        
