# from typing import Annotated

from fastapi import FastAPI,HTTPException,status
from sqlmodel import select


from .routers import users, blogs
from .dependencies import SessionDep
from .database import create_db_and_tables 

# from . import database
from . import schemas
from . import models
from .hashing import Hash


app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


app.include_router(users.router)
app.include_router(blogs.router)

