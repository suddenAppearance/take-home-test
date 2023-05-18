import logging
from typing import Callable

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker, Session

import settings

logger = logging.getLogger("api")

Base = declarative_base()

async_engine = create_async_engine(settings.DatabaseSettings().get_async_url().url)
sync_engine = create_engine(settings.DatabaseSettings().get_sync_url().url)

create_async_session: Callable[[], AsyncSession] = sessionmaker(
    bind=async_engine, expire_on_commit=False, class_=AsyncSession
)
create_session: Callable[[], Session] = sessionmaker(bind=sync_engine, expire_on_commit=False)
