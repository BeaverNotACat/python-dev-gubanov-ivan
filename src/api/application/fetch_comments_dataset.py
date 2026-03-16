from dataclasses import dataclass
from typing import final

from src.api.application.common.interactor import Interactor
from src.api.application.common.repositories import (
    CommentsDatasetDTO,
    CommentsDatasetRepositoryI,
)


@dataclass
class FetchCommentsDatasetDTO:
    login_filter: str


FetchCommentsDatasetResultDTO = tuple[CommentsDatasetDTO, ...]


@final
@dataclass(frozen=True)
class FetchCommentsDataset(
    Interactor[FetchCommentsDatasetDTO, FetchCommentsDatasetResultDTO]
):
    comment_repo: CommentsDatasetRepositoryI

    async def __call__(
        self, context: FetchCommentsDatasetDTO
    ) -> FetchCommentsDatasetResultDTO:
        return await self.comment_repo.fetch_dataset(
            login=context.login_filter
        )
