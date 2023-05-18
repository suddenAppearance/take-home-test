import logging
from asyncio import shield
from logging import Logger

from sqlalchemy.exc import DBAPIError
from sqlalchemy.ext.asyncio import AsyncSession

from models import create_async_session
from settings import Settings

settings = Settings()


def get_logger() -> Logger:
    return logging.getLogger("api")


def get_settings() -> Settings:
    return settings


async def get_session():
    session: AsyncSession = create_async_session()
    try:
        yield session
        await session.commit()
    except Exception:
        await session.rollback()
        raise
    finally:
        if session:
            await shield(session.close())
