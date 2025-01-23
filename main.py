from fastapi import FastAPI
from controller import items
from controller import users
app = FastAPI()

app.include_router(items.router)
app.include_router(users.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
