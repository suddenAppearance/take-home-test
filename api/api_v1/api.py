from fastapi import APIRouter

from api.api_v1.endpoints.survey import router as survey_router

router = APIRouter()

router.include_router(survey_router, prefix="/compensation_data", tags=["survey"])
