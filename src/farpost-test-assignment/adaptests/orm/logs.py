from datetime import datetime
from enum import StrEnum

from sqlalchemy import DateTime, ForeignKey, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column

from .base import BASE_INT_ID_TYPE, BaseORM


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


class SpaceTypeORM(BaseORM):
    id: Mapped[int] = mapped_column(
        SmallInteger, primary_key=True, autoincrement=True
    )
    name: Mapped[str]


class EventTypeORM(BaseORM):
    id: Mapped[int] = mapped_column(
        SmallInteger, primary_key=True, autoincrement=True
    )
    name: Mapped[str]


class LogORM(BaseORM):
    datetime: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    user_id: Mapped[int] = mapped_column(BASE_INT_ID_TYPE)
    space_type_id: Mapped[int] = mapped_column(ForeignKey(SpaceTypeORM.id))
    event_type_id: Mapped[int] = mapped_column(ForeignKey(EventTypeORM.id))
