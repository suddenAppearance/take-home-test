from logging import Logger
from typing import Type, TypeVar

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.requests import Request

from api.api_v1.deps import get_logger, get_session, get_settings
from repositories.survey import SurveyRepository
from settings import Settings

T = TypeVar('T')


class BaseService:
    def __init__(
        self,
        request: Request,
        session: AsyncSession = Depends(get_session),
        logger: Logger = Depends(get_logger),
        settings: Settings = Depends(get_settings),
    ):
        # base
        self.request = request
        self.session = session
        self.logger = logger
        self.settings = settings

    def factory(self, cls: Type[T], placeholder: str) -> T:
        if not hasattr(self.request, placeholder):
            setattr(self.request, placeholder, cls(self.request, self.session, self.logger, self.settings))

        service: T = getattr(self.request, placeholder)
        return service

    def repo_factory(self, cls: Type[T], placeholder: str) -> T:
        if not hasattr(self.request, placeholder):
            setattr(self.request, placeholder, cls(self.session))

        repo: T = getattr(self.request, placeholder)
        return repo


class SalaryServiceMixin(BaseService):
    @property
    def survey_service(self):
        from services.survey import SurveyService

        return self.factory(SurveyService, "_survey_service")

    @property
    def survey_repository(self):
        return self.repo_factory(SurveyRepository, "_survey_repository")
