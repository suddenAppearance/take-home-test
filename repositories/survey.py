from sqlalchemy import select

from models import SurveyResult
from repositories.base import BaseRepository


class SurveyRepository(BaseRepository[SurveyResult]):
    async def get_all(self, selects: list, filters: list, sorts: list ) -> list[SurveyResult]:
        statement = select(*(selects if selects else [SurveyResult])).filter(*filters).order_by(*sorts, SurveyResult.id).limit(20)

        if selects:
            return (await self.execute(statement)).all()
        else:
            return await self.all(statement)
