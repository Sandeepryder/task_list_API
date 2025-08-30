from fastapi import FastAPI
from app.routers import router as task_router


app = FastAPI()

@app.get("/")
def start():
    return {"message":"helo"}


app.include_router(task_router)