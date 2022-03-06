from db import models
from db.database import engine
from fastapi import FastAPI
from routes import user
import uvicorn
import sys
import os
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:8000",
    "http://localhost:3306",
    "https://localhost:3306",
]
os_origins = os.getenv('ALLOW_ORIGINS', '*')
origins = os_origins.split(',')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
sys.setrecursionlimit(3600)


@app.get("/")
def root():
    return "hello"

app.include_router(user.router)

models.Base.metadata.create_all(engine)

