from typing import NewType

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
)

AppAsyncEngine = NewType("AppAsyncEngine", AsyncEngine)
AppSessionMaker = NewType("AppSessionMaker", async_sessionmaker[AsyncSession])
AppSession = NewType("AppSession", AsyncSession)

LogsAsyncEngine = NewType("LogsAsyncEngine", AsyncEngine)
LogsSessionMaker = NewType(
    "LogsSessionMaker", async_sessionmaker[AsyncSession]
)
LogsSession = NewType("LogsSession", AsyncSession)
