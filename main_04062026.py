
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field

class StudentRequest(BaseModel):
    id:int = Field(title="ID",description="used to provide id")
    name:str = Field(title="Name",description="used to provide name")

class StudentResponse(BaseModel):
    id:int

obj = FastAPI(title="CodeMines Management System API",
              description="API contains all api related request and responses",
              version="V1.0.0")


@obj.get("/student/get/all",tags=["Student"],summary="used to get all student data")
def student_get_all():
    return JSONResponse(status_code=200,content={"data":"success"})

@obj.get("/student/get/{id}",tags=["Student"],summary="used to get student data by id")
def student_get_by_id(id:int):
    return JSONResponse(status_code=200,content={"data":"success"})

@obj.post("/student/insert",tags=["Student"],summary="used to insert new student data")
def student_insert(request:StudentRequest):
    response = StudentResponse(id=1234)
    return JSONResponse(status_code=200,content={"data":response.model_dump()})

@obj.get("/teacher/get/all",tags=["teacher"])
def teacher_get_all(name):
    return JSONResponse(status_code=200,content={"data":"success"})

@obj.get("/teacher/get/{id}",tags=["teacher"])
def teacher_get_by_id(id:int):
    return JSONResponse(status_code=200,content={"data":"success"})

@obj.post("/teacher/insert",tags=["teacher"])
def teacher_insert():
    return JSONResponse(status_code=200,content={"data":"success"})
    
