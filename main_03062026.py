
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

obj = FastAPI()

class StudentRequest(BaseModel):
    id:int
    name:str
    mobile:str
    email:str
    address:str

class StudentResponse(BaseModel):
    id:int
    name:str
    mobile:str
    email:str
    address:str
    enrollid:str

class LoginRequest(BaseModel):
    user:str
    password:str


# get request data from query paramater
@obj.get("/single-param")
def single_param(name):
    message = "Welcome "+name
    return JSONResponse(status_code=200,content={"data":message})

@obj.get("/multi-param")
def multi_param(id:int,name:str,mobile:str,email:str="",address:str=""):
    try:
        message = "ID: "+ str(id)+", Name: "+name+", Email: "+email+", Mobile: "+mobile+", Address: "+address
        return JSONResponse(status_code=200,content={"data":message})
    except Exception as e:
        return JSONResponse(status_code=500,content={"data": str(e)})
    
# get request data from path paramater
@obj.get("/single-path-param/{name}/details")
def single_path_param(name):
    message = "Welcome "+name
    return JSONResponse(status_code=200,content={"data":message})

@obj.get("/multi-path-param/{id}/{name}/details")
def multi_path_param(id:int,name:str):
    try:
        message = "ID: "+ str(id)+", Name: "+name
        return JSONResponse(status_code=200,content={"data":message})
    except Exception as e:
        return JSONResponse(status_code=500,content={"data": str(e)})
    

# get request data from path paramater
@obj.get("/query-path-param/{id}/{name}/details")
def single_path_param(id:int,name:str,mobile:str):
    message = "ID: "+ str(id)+", Name: "+name+", Mobile: "+mobile
    return JSONResponse(status_code=200,content={"data":message})


@obj.post("/details")
def details(details:StudentRequest):
    try:
        return JSONResponse(status_code=200,content={"data":details.model_dump()})
    except Exception as e:
        return JSONResponse(status_code=500,content={"data":str(e)})

@obj.get("/get-login")
def get_login(user:str,password:str):
    try:
        if user=="admin" and password=="admin@123":
            return JSONResponse(status_code=200,content={"data":"Login Successfull"})
        else:
            return JSONResponse(status_code=401,content={"data":"Invalid Username or password"})
    except Exception as e:
        return JSONResponse(status_code=500,content={"data":str(e)})

@obj.post("/post-login")
def post_login(login:LoginRequest):
    try:
        if login.user=="admin" and login.password=="admin@123":
            return JSONResponse(status_code=200,content={"data":"Login Successfull"})
        else:
            return JSONResponse(status_code=401,content={"data":"Invalid Username or password"})
    except Exception as e:
        return JSONResponse(status_code=500,content={"data":str(e)})

@obj.post("/insert")
def insert_data(request:StudentRequest):
    response = StudentResponse(
        id = request.id,
        name = request.name,
        mobile = request.mobile,
        email = request.email,
        address = request.address,
        enrollid = "EID12345"
    )
    return JSONResponse(status_code=201,content={"status":"success","data":response.model_dump()})

@obj.delete("/delete")
def delete_data(id:int):
    message="data deleted with id "+str(id)
    return JSONResponse(status_code=200,content={"status":"success","data":message})

@obj.put("/put")
def put_data(request:StudentRequest):
    response = StudentResponse(
        id = request.id,
        name = request.name,
        mobile = request.mobile,
        email = request.email,
        address = request.address,
        enrollid = "EID12345"
    )
    return JSONResponse(status_code=201,content={"status":"success","data":response.model_dump(),"message":"data updated successfully"})

@obj.patch("/patch")
def patch_data(request:StudentRequest):
    response = StudentResponse(
        id = request.id,
        name = request.name,
        mobile = request.mobile,
        email = request.email,
        address = request.address,
        enrollid = "EID12345"
    )
    return JSONResponse(status_code=201,content={"status":"success","data":response.model_dump(),"message":"data updated successfully"})

@obj.get("/forbidden-path-param/{name}/details")
def forbidden_path_param(name):
    if name=="admin":
        return JSONResponse(status_code=200,content={"data":"success"})
    else:
        return JSONResponse(status_code=403,content={"data":"you are not authorised to access this resource"})

