from typing import Any

from pydantic import BaseModel


class CodeAnalysisRequest(BaseModel):
    code: str
    language: str


class BasicAnalysisResponse(BaseModel):
    result: int


class DetailedAnalysisResponse(BasicAnalysisResponse):
    language: str
    classification: str
    features: dict[str, Any]
