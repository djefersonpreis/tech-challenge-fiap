from fastapi import APIRouter
from fastapi import Request, status
from fastapi.responses import RedirectResponse

import os

router = APIRouter()

@router.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url='/docs', status_code=status.HTTP_302_FOUND)

@router.get("/health", include_in_schema=False)
async def health_check():
    return {"status": "healthy"}

@router.get("/version", include_in_schema=False)
async def version_check():
    return {"version": os.getenv('API_VERSION', '') or 'undefined'}