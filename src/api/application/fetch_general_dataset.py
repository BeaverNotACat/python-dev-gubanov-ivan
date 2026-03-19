from dataclasses import dataclass
from typing import final

from src.api.application.common.interactor import Interactor
from src.api.application.common.repositories import (
    GeneralDatasetDTO,
    GeneralDatasetRepositoryI,
    UsersRepositoryI,
)


@dataclass
class FetchGeneralDatasetDTO:
    login_filter: str


FetchGeneralDatasetResultDTO = tuple[GeneralDatasetDTO, ...]


@final
@dataclass(frozen=True)
class FetchGeneralDataset(
    Interactor[FetchGeneralDatasetDTO, FetchGeneralDatasetResultDTO]
):
    statistics_repo: GeneralDatasetRepositoryI
    user_repo: UsersRepositoryI

    async def __call__(
        self, context: FetchGeneralDatasetDTO
    ) -> FetchGeneralDatasetResultDTO:
        user_id = await self.user_repo.fetch_user_id(
            login=context.login_filter
        )
        return await self.statistics_repo.fetch_dataset(user_id=user_id)
