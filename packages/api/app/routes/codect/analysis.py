from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from packages.core.python.javascript_analyzer import analyze_javascript_code
from packages.core.python.python_analyzer import analyze_python_code

from app.enums import Language
from app.models.analysis import BasicAnalysisResponse, CodeAnalysisRequest, DetailedAnalysisResponse

analysis_router = APIRouter(prefix="/analysis", tags=["analysis"])


def _analyze_code(code: str, language: str) -> tuple[dict, str, int]:
    if language.lower() not in list(Language):
        raise HTTPException(status_code=400, detail=f"Unsupported language: {language}")

    language = Language(language.lower())
    languages_analyzers = {
        Language.PYTHON: analyze_python_code,
        Language.JAVASCRIPT: analyze_javascript_code,
    }

    try:
        features, classification = languages_analyzers[language](code)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {e}")

    # TODO: Update analyzers to return integer or bool for result
    result = 1 if classification == "AI-Generated Code" else 0
    return features, classification, result


@analysis_router.post("/basic", response_model=BasicAnalysisResponse)
async def basic_analysis(request: CodeAnalysisRequest):
    _, _, result = _analyze_code(request.code, request.language)
    return BasicAnalysisResponse(result=result)


@analysis_router.post("/premium", response_model=DetailedAnalysisResponse)
async def premium_analysis(request: CodeAnalysisRequest):
    # TODO: Check permissions
    features, classification, result = _analyze_code(request.code, request.language)
    return DetailedAnalysisResponse(
        result=result,
        language=request.language,
        classification=classification,
        features=features,
    )
