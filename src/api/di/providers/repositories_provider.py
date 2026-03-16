from dishka import Provider, Scope

from src.api.adapters.repositories import (
    CommentsDatasetRepository,
    StatisticsDatasetRepository,
    UsersRepository,
)
from src.api.application.common.repositories import (
    CommentsDatasetRepositoryI,
    StatisticsDatasetRepositoryI,
    UsersRepositoryI,
)

repositories_provider = Provider(scope=Scope.REQUEST)
repositories_provider.provide(
    CommentsDatasetRepository, provides=CommentsDatasetRepositoryI
)
repositories_provider.provide(
    StatisticsDatasetRepository, provides=StatisticsDatasetRepositoryI
)
repositories_provider.provide(UsersRepository, provides=UsersRepositoryI)
