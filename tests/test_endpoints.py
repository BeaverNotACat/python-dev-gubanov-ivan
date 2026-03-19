from typing import TYPE_CHECKING

from litestar.status_codes import HTTP_200_OK
from litestar.testing import AsyncTestClient

if TYPE_CHECKING:
    from litestar import Litestar


async def test_get_comments(test_client: AsyncTestClient[Litestar]) -> None:
    response = await test_client.get("/api/comments?login=login")
    assert response.status_code == HTTP_200_OK


async def test_get_statistics(test_client: AsyncTestClient[Litestar]) -> None:
    response = await test_client.get("/api/general?login=login")
    assert response.status_code == HTTP_200_OK
