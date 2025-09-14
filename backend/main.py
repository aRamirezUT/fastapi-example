from fastapi import FastAPI

from .dependencies import lifespan
from .internal import admin
from .routers import campaigns

app = FastAPI(root_path="/api/v1", lifespan=lifespan)

app.include_router(campaigns.router)
app.include_router(admin.router)

@app.get("/")
async def root():
    return {"message": "Hello, world!"}