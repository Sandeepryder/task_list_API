from fastapi import FastAPI
from app.routers import router as task_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/")
def start():
    return {"message":"helo"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(task_router)