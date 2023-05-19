from fastapi import APIRouter, Depends, Query
from fastapi.requests import Request

from schemas.survey import SurveyResultSchema
from services.survey import SurveyService

router = APIRouter()


@router.get("/", response_model=list[SurveyResultSchema], response_model_exclude_none=True)
async def get_all(request: Request, service: SurveyService = Depends(), sort: list[str] = Query([]), fields: list[str] | None= Query(None)):
    params = dict(request.query_params)
    params.pop("sort", None)
    params.pop("fields", None)

    return await service.get_all(filters=params, sorts=sort, fields=fields)
