from fastapi import APIRouter

from app.routes.codect.analysis import analysis_router

codect_router = APIRouter(prefix="/codect")
codect_router.include_router(analysis_router)


@codect_router.get("/")
async def codect_root():
    return {
        "message": "Codect API",
        "endpoints": {
            "/basic": "Basic analysis - returns only the classification result",
            "/premium": "Detailed analysis - returns classification and all features",
        },
    }
