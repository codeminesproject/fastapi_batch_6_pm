
from fastapi import FastAPI
from fastapi.responses import JSONResponse

obj = FastAPI()


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

