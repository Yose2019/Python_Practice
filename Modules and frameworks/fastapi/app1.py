from fastapi import FastAPI

app = FastAPI() # creating an instance of fast api 

@app.get("/")
def greet():
    return "Say hello"

@app.get("/bye")
def bye():
    return "bye bye"
