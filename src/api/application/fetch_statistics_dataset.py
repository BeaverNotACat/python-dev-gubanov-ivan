from dataclasses import dataclass
from typing import final

from src.api.application.common.interactor import Interactor
from src.api.application.common.repositories import (
    StatisticsDatasetDTO,
    StatisticsDatasetRepositoryI,
    UsersRepositoryI,
)


@dataclass
class FetchStatisticsDatasetDTO:
    login_filter: str


FetchStatisticsDatasetResultDTO = tuple[StatisticsDatasetDTO, ...]


@final
@dataclass(frozen=True)
class FetchStatisticsDataset(
    Interactor[FetchStatisticsDatasetDTO, FetchStatisticsDatasetResultDTO]
):
    statistics_repo: StatisticsDatasetRepositoryI
    user_repo: UsersRepositoryI

    async def __call__(
        self, context: FetchStatisticsDatasetDTO
    ) -> FetchStatisticsDatasetResultDTO:
        user_id = await self.user_repo.fetch_user_id(
            login=context.login_filter
        )
        return await self.statistics_repo.fetch_dataset(user_id=user_id)
