from dishka.integrations.litestar import FromDishka, inject
from litestar import Router, get
from litestar.dto import DataclassDTO

from src.api.application.fetch_comments_dataset import (
    FetchCommentsDataset,
    FetchCommentsDatasetDTO,
    FetchCommentsDatasetResultDTO,
)
from src.api.application.fetch_general_dataset import (
    FetchGeneralDataset,
    FetchGeneralDatasetDTO,
    FetchGeneralDatasetResultDTO,
)


@get("/comments", return_dto=DataclassDTO[FetchCommentsDatasetResultDTO])
@inject
async def get_comments(
    login: str, interactor: FromDishka[FetchCommentsDataset]
) -> FetchCommentsDatasetResultDTO:
    context = FetchCommentsDatasetDTO(login_filter=login)
    return await interactor(context)


@get("/general", return_dto=DataclassDTO[FetchGeneralDatasetResultDTO])
@inject
async def get_statistics(
    login: str, interactor: FromDishka[FetchGeneralDataset]
) -> FetchGeneralDatasetResultDTO:
    context = FetchGeneralDatasetDTO(login_filter=login)
    return await interactor(context)


api_router = Router(path="/api", route_handlers=[get_comments, get_statistics])
