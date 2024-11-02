from fastapi import FastAPI 


app = FastAPI()


@app.get('/')
def index():
    return "Hello World!!"


@app.get('/about')
def about():
    return ({"data": {"First Name":"George","Last name": "Chempumthara"}})