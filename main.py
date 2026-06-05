
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field
from typing import List

class Subjects(BaseModel):
    id:int
    name:str

class StudentRequest(BaseModel):
    id:int
    name:str
    subject:Subjects

class StudentRequests(BaseModel):
    id:int
    name:str
    subject:List[Subjects]

class StudentResponse(BaseModel):
    id:int
    subject:List[Subjects] 

class Request1(BaseModel):
    id:int
    username:str
    password:str

class Request2(BaseModel):
    ip_address:str
    status:str

obj = FastAPI()



@obj.post("/student/insert")
def student_insert(request:StudentRequests):
    response = StudentResponse(
        id=request.id,
        subject = request.subject
        )
    return JSONResponse(status_code=200,content={"data":response.model_dump()})



@obj.post("/student/insert/1")
def student_insert_1(request1:Request1,request2:Request2):
    return JSONResponse(status_code=200)

