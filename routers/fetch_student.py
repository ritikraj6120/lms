from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from bson.objectid import ObjectId
from datamodels.student import StudentModel
api_router = APIRouter()


@api_router.get("/{id}", response_model=StudentModel)
def fetch_student(id: str, request: Request):
    try:
        student = request.app.database["students"].find_one({"_id": ObjectId(id)})
        if student:
            return StudentModel(**student)
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error retrieving the student.")