
from typing import Optional
import uuid;
from pydantic import BaseModel, Field, PositiveInt

class Address(BaseModel):
    city:Optional[str] = Field(min_length=1,examples="Hyderabad", title = "city")
    country:Optional[str] = Field(min_length=1,examples = "Telangana", title = "country")
    
class UpdateStudentModel(BaseModel):
    name: Optional[str] = Field(min_length=1,examples="Ritik Raj",title = "name")
    age: Optional[PositiveInt]  = Field(examples=10,title = "age")
    address: Optional[Address]