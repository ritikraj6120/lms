from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from datamodels.student import StudentModel
from datamodels.responses.created_student_response import CreatedStudentResponseModel

api_router = APIRouter()

@api_router.post("/", response_description='A JSON response sending back the ID of the newly created student record.', status_code=status.HTTP_201_CREATED)
def create_student(request: Request,input_model:StudentModel) -> CreatedStudentResponseModel :
	try:
		input_model = jsonable_encoder(input_model)
		new_student = request.app.database["students"].insert_one(input_model)
		return CreatedStudentResponseModel(id = str(new_student.inserted_id))
		# return CreatedStudentResponseModel(str(new_student.inserted_id))
	except Exception as e:
		raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=f"Caught Error: [{e}]")