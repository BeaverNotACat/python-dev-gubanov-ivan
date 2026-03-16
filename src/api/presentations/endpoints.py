from dishka.integrations.litestar import FromDishka, inject
from litestar import Router, get
from litestar.dto import DataclassDTO

from src.api.application.fetch_comments_dataset import (
    FetchCommentsDataset,
    FetchCommentsDatasetDTO,
    FetchCommentsDatasetResultDTO,
)
from src.api.application.fetch_statistics_dataset import (
    FetchStatisticsDataset,
    FetchStatisticsDatasetDTO,
    FetchStatisticsDatasetResultDTO,
)


@get("/comments", return_dto=DataclassDTO[FetchCommentsDatasetResultDTO])
@inject
async def get_comments(
    login: str, interactor: FromDishka[FetchCommentsDataset]
) -> FetchCommentsDatasetResultDTO:
    context = FetchCommentsDatasetDTO(login_filter=login)
    return await interactor(context)


@get("/statistics", return_dto=DataclassDTO[FetchStatisticsDatasetResultDTO])
@inject
async def get_statistics(
    login: str, interactor: FromDishka[FetchStatisticsDataset]
) -> FetchStatisticsDatasetResultDTO:
    context = FetchStatisticsDatasetDTO(login_filter=login)
    return await interactor(context)


api_router = Router(path="/api", route_handlers=[get_comments, get_statistics])
