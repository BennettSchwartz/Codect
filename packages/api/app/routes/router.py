from fastapi import APIRouter

codect_router = APIRouter(prefix="/codect")


@codect_router.get("/")
async def codect_root():
    return {
        "message": "Codect API",
        "endpoints": {
            "/basic": "Basic analysis - returns only the classification result",
            "/premium": "Detailed analysis - returns classification and all features",
            "/health": "Health check endpoint",
        },
    }
