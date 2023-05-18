from sqlalchemy import select

from models import SurveyResult
from repositories.base import BaseRepository


class SurveyRepository(BaseRepository[SurveyResult]):
    async def get_all(self, filters: list, sorts: list ) -> list[SurveyResult]:
        statement = select(SurveyResult).filter(*filters).order_by(*sorts, SurveyResult.id).limit(20)
        return await self.all(statement)
