from fastapi import APIRouter 
from .base_routes import router as base_router
from .embrapa_routes import router as embrapa_router

router = APIRouter()

router.include_router(base_router, tags=["base"])
router.include_router(embrapa_router, tags=["Embrapa"])