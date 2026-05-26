from fastapi import FastAPI

from routes.bubbletea import router as bubbletea_router

app = FastAPI()

@app.get("/")
def say_hello():
    return {"message": "Hello, World!"}

app.include_router(bubbletea_router)
