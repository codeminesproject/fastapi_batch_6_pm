
from fastapi import FastAPI
from fastapi.responses import JSONResponse

obj = FastAPI()

@obj.get("/display")
def display_message():
    return JSONResponse(content={"data":"Welcome To CodeMines"})

@obj.get("/message")
def greet():
    return JSONResponse(content={"data":"Hello"})