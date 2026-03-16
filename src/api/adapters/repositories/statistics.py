from datetime import date

from sqlalchemy import Select, and_, func, select
from sqlalchemy.orm import aliased

from src.api.adapters.engines import LogsSession
from src.api.adapters.orm.logs import (
    EventType,
    EventTypeORM,
    LogORM,
    SpaceType,
    SpaceTypeORM,
)
from src.api.application.common.repositories import (
    StatisticsDatasetDTO,
    StatisticsDatasetRepositoryI,
)


class StatisticsDatasetRepository(StatisticsDatasetRepositoryI):
    def __init__(self, session: LogsSession) -> None:
        self.session = session

    async def fetch_dataset(
        self, *, user_id: int
    ) -> tuple[StatisticsDatasetDTO, ...]:
        query = self._construct_query(user_id)
        res = await self.session.execute(query)
        return tuple(
            StatisticsDatasetDTO(
                row.date,
                row.logins_amount,
                row.logouts_amount,
                row.blog_actions_amount,
            )
            for row in res
        )

    @staticmethod
    def _construct_query(user_id: int) -> Select[tuple[date, int, int, int]]:
        date_logs = aliased(LogORM)

        login_logs = aliased(LogORM)
        login_event_type = aliased(EventTypeORM)

        logout_logs = aliased(LogORM)
        logout_event_type = aliased(EventTypeORM)

        blog_logs = aliased(LogORM)
        blog_space_type = aliased(SpaceTypeORM)

        return (
            select(
                func.Date(date_logs.datetime).label("date"),
                func.count(login_logs.id).label("logins_amount"),
                func.count(logout_logs.id).label("logouts_amount"),
                func.count(blog_logs.id).label("blog_actions_amount"),
            )
            .group_by("date")
            .join(login_event_type, login_event_type.name == EventType.LOGIN)
            .outerjoin(
                login_logs,
                and_(
                    login_logs.event_type_id == login_event_type.id,
                    login_logs.user_id == user_id,
                    func.Date(login_logs.datetime)
                    == func.Date(date_logs.datetime),
                ),
            )
            .join(
                logout_event_type, logout_event_type.name == EventType.LOGOUT
            )
            .outerjoin(
                logout_logs,
                and_(
                    logout_logs.event_type_id == logout_event_type.id,
                    logout_logs.user_id == user_id,
                    func.Date(logout_logs.datetime)
                    == func.Date(date_logs.datetime),
                ),
            )
            .join(blog_space_type, blog_space_type.name == SpaceType.BLOG)
            .outerjoin(
                blog_logs,
                and_(
                    blog_logs.space_type_id == blog_space_type.id,
                    blog_logs.user_id == user_id,
                    func.Date(blog_logs.datetime)
                    == func.Date(date_logs.datetime),
                ),
            )
            .select_from(date_logs)
            .where(date_logs.user_id == user_id)
        )
