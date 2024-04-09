from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from bson.objectid import ObjectId
api_router = APIRouter()

@api_router.delete("/{id}")
def delete_student(id:str,request: Request) :
	try:
		deleted_student =  request.app.database["students"].delete_one({"_id": ObjectId(id)})
		if deleted_student.deleted_count==1:
			return {"message": "Student deleted successfully"}
		else:
			raise HTTPException(status_code=404, detail="Student not found")
	except Exception as e:
		raise e