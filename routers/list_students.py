from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from bson.objectid import ObjectId
from typing import Optional,List
from datamodels.student import StudentModel
api_router = APIRouter()


@api_router.get("/", response_model=List[StudentModel])
def list_students(request: Request,country: Optional[str] = None, age: Optional[int] = None):
    try:
        filter_query = {}
        if country:
            filter_query["address.country"] = country
        if age:
            filter_query["age"] = {"$gte": age}
        students = list(request.app.database["students"].find(filter_query))
        return [StudentModel( **student) for student in students]
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error retrieving the students.")