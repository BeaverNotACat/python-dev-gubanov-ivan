from sqlalchemy import Select, func, select
from sqlalchemy.orm import aliased

from src.api.adapters.connections import AppSession
from src.api.adapters.orm.app import CommentORM, PostORM, UserORM
from src.api.application.common.repositories.comments import (
    CommentsDatasetDTO,
    CommentsDatasetRepositoryI,
)


class CommentsDatasetRepository(CommentsDatasetRepositoryI):
    def __init__(self, session: AppSession) -> None:
        self.session = session

    async def fetch_dataset(
        self, *, login: str
    ) -> tuple[CommentsDatasetDTO, ...]:
        query = self._construct_query(login)
        res = await self.session.execute(query)
        return tuple(
            CommentsDatasetDTO(
                row.login,
                row.post_header,
                row.post_author,
                row.comments_amount,
            )
            for row in res
        )

    @staticmethod
    def _construct_query(login: str) -> Select[tuple[str, str, str, int]]:
        commenter = aliased(UserORM)
        authors = aliased(UserORM)
        featured_comment = aliased(CommentORM)
        all_comments = aliased(CommentORM)

        return (
            select(
                commenter.login,
                PostORM.header.label("post_header"),
                authors.login.label("post_author"),
                func.count(all_comments.id).label("comments_amount"),
            )
            .group_by(commenter.login, PostORM.header, authors.login)
            .join(featured_comment, featured_comment.author_id == commenter.id)
            .join(PostORM, PostORM.id == featured_comment.post_id)
            .join(authors, authors.id == PostORM.author_id)
            .join(all_comments, all_comments.post_id == PostORM.id)
            .where(commenter.login == login)
        )
