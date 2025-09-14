from fastapi import APIRouter

from backend.main import lifespan

router = APIRouter(prefix="/admin", lifespan=lifespan, tags=["admin"])

@router.get("/")
async def get_admin():
    return {"message": "Admin getting schwifty"}