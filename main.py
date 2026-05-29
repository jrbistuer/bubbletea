from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.bubbletea import router as bubbletea_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost", "http://127.0.0.1"],
    allow_origin_regex=r"https?://(localhost|127\.0\.0\.1)(:\d+)?$",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def say_hello():
    return {"message": "Hello, World!"}

app.include_router(bubbletea_router)
