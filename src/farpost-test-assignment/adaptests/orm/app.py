from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseORM


class UserORM(BaseORM):
    __tablename__ = "users"
    email: Mapped[str] = mapped_column(String(320))
    login: Mapped[str] = mapped_column(unique=True)


class BlogORM(BaseORM):
    __tablename__ = "blogs"
    name: Mapped[str]
    description: Mapped[str]

    owner_id: Mapped[int] = mapped_column(ForeignKey(UserORM.id))


class PostORM(BaseORM):
    header: Mapped[str]
    text: Mapped[str]

    author_id: Mapped[int] = mapped_column(ForeignKey(UserORM.id))
    blog_id: Mapped[int] = mapped_column(ForeignKey(BlogORM.id))
