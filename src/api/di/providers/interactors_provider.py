from dishka import Provider, Scope

from src.api.application.fetch_comments_dataset import FetchCommentsDataset
from src.api.application.fetch_general_dataset import FetchGeneralDataset

interactors_provider = Provider(scope=Scope.REQUEST)
interactors_provider.provide(FetchCommentsDataset)
interactors_provider.provide(FetchGeneralDataset)
