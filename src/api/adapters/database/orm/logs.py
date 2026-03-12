from datetime import datetime
from enum import StrEnum

from sqlalchemy import BigInteger, DateTime, ForeignKey, SmallInteger
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from .app import BASE_APP_ID_TYPE


class LogsBaseORM(AsyncAttrs, DeclarativeBase):
    """
    AppBase ORM class with ID as BASE_ID_TYPE(int8)
    """

    id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True, autoincrement=True
    )


class SpaceType(StrEnum):
    GLOBAL = "global"
    BLOG = "blog"
    POST = "post"


class EventType(StrEnum):
    LOGIN = "login"
    COMMENT = "comment"
    CREATE_POST = "create_post"
    DELETE_POST = "delete_post"
    LOGOUT = "logout"


class SpaceTypeORM(LogsBaseORM):
    __tablename__ = "space_types"

    id: Mapped[int] = mapped_column(
        SmallInteger, primary_key=True, autoincrement=True
    )
    name: Mapped[str]


class EventTypeORM(LogsBaseORM):
    __tablename__ = "event_types"

    id: Mapped[int] = mapped_column(
        SmallInteger, primary_key=True, autoincrement=True
    )
    name: Mapped[str]


class LogORM(LogsBaseORM):
    __tablename__ = "logs"

    datetime: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    user_id: Mapped[int] = mapped_column(BASE_APP_ID_TYPE)
    space_type_id: Mapped[int] = mapped_column(ForeignKey(SpaceTypeORM.id))
    event_type_id: Mapped[int] = mapped_column(ForeignKey(EventTypeORM.id))
