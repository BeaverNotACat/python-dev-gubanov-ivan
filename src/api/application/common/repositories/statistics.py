from abc import abstractmethod
from dataclasses import dataclass
from datetime import date
from typing import Protocol


@dataclass(frozen=True, slots=True)
class StatisticsDatasetDTO:
    date: date
    logins_amount: int
    logouts_amount: int
    blog_actions_amount: int


class StatisticsDatasetRepositoryI(Protocol):
    @abstractmethod
    async def fetch_dataset(
        self, *, user_id: int
    ) -> tuple[StatisticsDatasetDTO, ...]:
        raise NotImplementedError
