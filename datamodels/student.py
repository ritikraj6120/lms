
from typing import Optional
import uuid;
from pydantic import BaseModel, Field, PositiveInt

class Address(BaseModel):
    city:str = Field(min_length=1,examples="Hyderabad", title = "city")
    country:str = Field(min_length=1,examples = "Telangana", title = "country")
    
class StudentModel(BaseModel):
    name: str = Field(min_length=1,examples="Ritik Raj",title = "name")
    age: PositiveInt  = Field(examples=10,title = "age")
    address: Address