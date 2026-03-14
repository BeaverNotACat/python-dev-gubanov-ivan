from polyfactory.factories.sqlalchemy_factory import (
    SQLAlchemyFactory,
)

from src.api.adapters.orm.app import BlogORM, CommentORM, PostORM, UserORM


class UserMockFactory(SQLAlchemyFactory[UserORM]):
    @classmethod
    def id(cls) -> None:
        return None

    @classmethod
    def email(cls) -> str:
        return cls.__faker__.email()

    # @classmethod
    # def login(cls) -> str:
    #     return cls.__faker__.user_name()


class BlogMockFactory(SQLAlchemyFactory[BlogORM]):
    @classmethod
    def id(cls) -> None:
        return None


class PostMockFactory(SQLAlchemyFactory[PostORM]):
    @classmethod
    def id(cls) -> None:
        return None


class CommentMockFactory(SQLAlchemyFactory[CommentORM]):
    @classmethod
    def id(cls) -> None:
        return None
