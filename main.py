from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from router_at_student import api_router as api_router_at_student
config = dotenv_values(".env")

app = FastAPI()


app.include_router(router = api_router_at_student)

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["MONGODB_CONNECTION_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]
    print("Connected to the MongoDB database!")

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()