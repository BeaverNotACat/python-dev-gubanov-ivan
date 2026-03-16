from sqlalchemy import BigInteger, ForeignKey, String
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
)

BASE_APP_ID_TYPE = BigInteger


class AppBaseORM(AsyncAttrs, DeclarativeBase):
    id: Mapped[int] = mapped_column(
        BASE_APP_ID_TYPE, primary_key=True, autoincrement=True
    )


class UserORM(AppBaseORM):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(String(320))
    login: Mapped[str] = mapped_column(unique=True)


class BlogORM(AppBaseORM):
    __tablename__ = "blogs"

    name: Mapped[str]
    description: Mapped[str]

    owner_id: Mapped[int] = mapped_column(ForeignKey(UserORM.id))


class PostORM(AppBaseORM):
    __tablename__ = "posts"

    header: Mapped[str]
    text: Mapped[str]

    author_id: Mapped[int] = mapped_column(ForeignKey(UserORM.id))
    blog_id: Mapped[int] = mapped_column(ForeignKey(BlogORM.id))


class CommentORM(AppBaseORM):
    __tablename__ = "comments"

    text: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey(UserORM.id), index=True)
    post_id: Mapped[int] = mapped_column(ForeignKey(PostORM.id), index=True)
