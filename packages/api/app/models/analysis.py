from typing import Any

from pydantic import BaseModel


class CodeAnalysisRequest(BaseModel):
    code: str
    language: str


class BasicAnalysisResponse(BaseModel):
    result: int


class DetailedAnalysisResponse(BaseModel):
    result: int
    language: str
    classification: str
    features: dict[str, Any]
