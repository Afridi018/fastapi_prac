from pydantic import BaseModel
from typing import Optional

class blogType (BaseModel):
    title: str
    age: Optional[int] = None
    description: str
    

class userType (BaseModel):
    email: str
    password: str
    

class userReponseType (BaseModel):
    id: int
    email: str    
    model_config = {
        "from_attributes": True
    }