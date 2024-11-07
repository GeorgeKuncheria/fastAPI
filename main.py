from fastapi import FastAPI 
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get('/blog')
def index(limit=10,published:bool = False,sort: Optional[str] = None  ):
    if published:
        return ({"data":f"{limit} published blogs from the list"})
    else:
        return ({"data": f"{limit} blogs from the list"})

# when creating routes DYNAMIC routes must be right below static ones

@app.get('/blog/unpublished')
def unpublished():
    return ({"data": "all unpublished data"})


@app.get('/blog/{id}')
def show(id:int):
    return ({"data": id})


@app.get('/blog/{id}/comments')
def show(id):
    return ({"data": {"1","2","3","4","5","6"}})


class Blog(BaseModel):
    title : str
    body : str
    published : Optional[bool]


@app.post('/blog')
def create_blog(blog : Blog):
    return ({'data':f"Blog post created  as {blog.title}  "})
