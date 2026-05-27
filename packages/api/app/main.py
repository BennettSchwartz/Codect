from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.router import codect_router

app = FastAPI(title="Codect API", description="AI-generated code detection API", version="0.1.0")

app.include_router(codect_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
