from fastapi import APIRouter

from routers import create_student,delete_student,fetch_student,list_students,update_student

prefix = "/students"

api_router = APIRouter(tags=["Student"],prefix = prefix)
api_router.include_router(create_student.api_router)
api_router.include_router(delete_student.api_router)
api_router.include_router(fetch_student.api_router)
api_router.include_router(list_students.api_router)
api_router.include_router(update_student.api_router)
