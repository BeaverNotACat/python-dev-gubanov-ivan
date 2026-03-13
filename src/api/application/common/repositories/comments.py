from abc import abstractmethod
from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True, slots=True)
class CommentsDatasetDTO:
    login: str
    post_header: str
    post_author: str
    comments_amount: int


class CommentsDatasetRepositoryI(Protocol):
    @abstractmethod
    async def fetch_dataset(
        self, login: str
    ) -> tuple[CommentsDatasetDTO, ...]:
        raise NotImplementedError
