import abc
import logging
from typing import Generic, TypeVar

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import Select, Update, Delete

logger = logging.getLogger("api")

T = TypeVar("T")


class BaseRepository(abc.ABC, Generic[T]):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def save(self, obj: T) -> T:
        self.session.add(obj)
        await self.session.flush()
        await self.session.refresh(obj)
        return obj

    async def one_or_none(self, statement):
        return (await self.session.execute(statement)).scalars().one_or_none()

    async def all(self, statement: Select):
        return (await self.session.execute(statement)).scalars().all()

    async def execute(self, statement: Select | Update | Delete):
        return await self.session.execute(statement)
