from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from bson.objectid import ObjectId
from typing import Optional,List
from datamodels.requests.update_student import UpdateStudentModel
api_router = APIRouter()

@api_router.patch("/{id}", status_code=204)
def update_student(id: str, student: UpdateStudentModel,request:Request):
    try:
        updated_student = request.app.database["students"].find_one_and_update(
            {"_id": ObjectId(id)},
            {"$set": student.dict()},
            return_document=True
        )
        if updated_student:
            return
        else:
            raise HTTPException(status_code=404, detail="Student not found")
    except Exception as e:
        raise e