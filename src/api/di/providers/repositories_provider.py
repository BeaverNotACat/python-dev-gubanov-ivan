from dishka import Provider, Scope

from src.api.adapters.repositories import (
    CommentsDatasetRepository,
    GeneralDatasetRepository,
    UsersRepository,
)
from src.api.application.common.repositories import (
    CommentsDatasetRepositoryI,
    GeneralDatasetRepositoryI,
    UsersRepositoryI,
)

repositories_provider = Provider(scope=Scope.REQUEST)
repositories_provider.provide(
    CommentsDatasetRepository, provides=CommentsDatasetRepositoryI
)
repositories_provider.provide(
    GeneralDatasetRepository, provides=GeneralDatasetRepositoryI
)
repositories_provider.provide(UsersRepository, provides=UsersRepositoryI)
