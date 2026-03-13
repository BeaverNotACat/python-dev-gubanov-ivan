from polyfactory.factories.sqlalchemy_factory import (
    SQLAlchemyFactory,
)

from src.api.adapters.orm.logs import LogORM


class LogMockFactory(SQLAlchemyFactory[LogORM]):
    @classmethod
    def id(cls) -> None:
        return None

    @classmethod
    def space_type_id(cls) -> int:
        return cls.__random__.randint(1, 3)

    @classmethod
    def event_type_id(cls) -> int:
        return cls.__random__.randint(1, 5)
