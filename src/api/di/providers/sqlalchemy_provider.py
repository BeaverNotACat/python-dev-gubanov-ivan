from collections.abc import AsyncIterable

from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from src.api.adapters.engines import (
    AppAsyncEngine,
    AppSession,
    AppSessionMaker,
    LogsAsyncEngine,
    LogsSession,
    LogsSessionMaker,
)
from src.api.settings import Settings


class AppAlchemyProvider(Provider):
    scope = Scope.APP

    @provide
    @staticmethod
    def get_app_alchemy_engine(settings: Settings) -> AppAsyncEngine:
        return AppAsyncEngine(
            create_async_engine(str(settings.APP_DATABASE_DSN))
        )

    @provide
    @staticmethod
    def get_app_alchemy_sessionmaker(
        engine: AppAsyncEngine,
    ) -> AppSessionMaker:
        return AppSessionMaker(async_sessionmaker(engine))

    @provide()
    @staticmethod
    async def get_app_session(
        session_maker: AppSessionMaker,
    ) -> AsyncIterable[AppSession]:
        session = session_maker()
        # TODO: Potential problems with transactions lifetime
        yield AppSession(session)
        await session.close()


class LogsAlchemyProvider(Provider):
    scope = Scope.APP

    @provide
    @staticmethod
    def get_logs_alchemy_engine(settings: Settings) -> LogsAsyncEngine:
        return LogsAsyncEngine(
            create_async_engine(str(settings.LOGS_DATABASE_DSN))
        )

    @provide
    @staticmethod
    def get_logs_alchemy_sessionmaker(
        engine: LogsAsyncEngine,
    ) -> LogsSessionMaker:
        return LogsSessionMaker(async_sessionmaker(engine))

    @provide()
    @staticmethod
    async def get_app_session(
        session_maker: LogsSessionMaker,
    ) -> AsyncIterable[LogsSession]:
        session = session_maker()
        # TODO: Potential problems with transactions lifetime
        yield LogsSession(session)
        await session.close()
