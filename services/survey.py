from typing import Any

from fastapi import HTTPException

from models import SurveyResult
from schemas.survey import SurveyResultSchema
from services.base import SalaryServiceMixin


class SurveyService(SalaryServiceMixin):
    @property
    def repository(self):
        return self.survey_repository

    async def get_all(
        self, filters: dict[str, str], sorts: list[str], fields: list[str] | None
    ) -> list[SurveyResultSchema]:
        filters_map = self.get_filters_map()
        filter_clauses = [filters_map[filter](self.auto_cast(value)) for filter, value in filters.items()]

        sort_clauses = [self.get_sort_clause(sort) for sort in sorts]

        return [
            SurveyResultSchema.from_orm(result)
            for result in await self.repository.get_all(
                selects=self.sparse_select(fields), filters=filter_clauses, sorts=sort_clauses
            )
        ]

    @staticmethod
    def sparse_select(fields: list[str] | None) -> Any:
        if not fields:
            return None

        selects = [SurveyResult.id]
        for field in fields:
            if field == 'id':
                continue

            if not hasattr(SurveyResult, field):
                raise HTTPException(status_code=400, detail=f"Unknown field {field}")

            selects.append(getattr(SurveyResult, field))

        return selects

    @staticmethod
    def auto_cast(val: str) -> Any:
        if val.isdigit():
            return int(val)
        if val == "false":
            return False
        if val == "true":
            return True
        if val == "null":
            return None

        try:
            return float(val)
        except ValueError:
            return val

    @staticmethod
    def get_filters_map() -> dict[str, Any]:
        return {
            col: lambda x, col=col: getattr(SurveyResult, col) == x for col in SurveyResultSchema.__fields__.keys()
        } | {
            "total_salary[gte]": lambda x: SurveyResult.total_salary >= x,
            "total_salary[lte]": lambda x: SurveyResult.total_salary <= x,
            "total_bonus[gte]": lambda x: SurveyResult.total_bonus >= x,
            "total_bonus[lte]": lambda x: SurveyResult.total_bonus <= x,
            "total_equity[gte]": lambda x: SurveyResult.total_salary >= x,
            "total_equity[lte]": lambda x: SurveyResult.total_salary <= x,
        }

    def get_sort_clause(self, sort: str) -> Any:
        sort_arr = sort.split()

        if len(sort_arr) > 2 or len(sort_arr) == 0:
            raise HTTPException(status_code=400, detail=f"Invalid sort {sort}")

        field, asc = (sort_arr[0], "asc") if len(sort_arr) == 1 else (sort_arr[0], sort_arr[1])

        if asc not in ["asc", "desc"]:
            raise HTTPException(status_code=400, detail=f"Invalid sort direction {asc}")

        if not hasattr(SurveyResult, field):
            raise HTTPException(status_code=400, detail=f"Invalid sort field {field}")

        return getattr(getattr(SurveyResult, field), asc)()
