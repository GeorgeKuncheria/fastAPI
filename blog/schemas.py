from pydantic import BaseModel
from typing import List



class Login(BaseModel):
    email : str
    password : str


class Blog(BaseModel):
    title : str
    body : str

    class Config():
        orm_mode= True


class User(BaseModel):
    name : str
    email : str
    password : str



class ShowUser(BaseModel):
    name : str
    email : str
    blogs: List[Blog]

    class Config():
        orm_mode= True

class CreatorInfo(BaseModel):
    name: str
    email: str

    class Config:
        orm_mode = True

# To show the title of the blog as a response instead of the whole blog data we use 'response_model' parameter
class ShowBlog(BaseModel):
    title : str
    body : str
    creator : CreatorInfo

    class Config():
        orm_mode = True
