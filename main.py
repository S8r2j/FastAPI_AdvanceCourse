from typing import Optional

from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app=FastAPI()


class Post(BaseModel):
    title:str
    content:str
    published:bool=True
    rating:Optional[int]=None


@app.get("/")
async def root():
    return{"message":"Hello world"}


@app.get("/posts")
def get_posts():
    return {"data":"This is your posts"}

@app.post("/createposts")
def create_post(body:Post):
    print(body)
    print(body.dict())
    return {"new post":body};