from collections.abc import AsyncIterator
from typing import TYPE_CHECKING

import pytest
from litestar.testing import AsyncTestClient

from src.api.app import app

if TYPE_CHECKING:
    from litestar import Litestar

app.debug = True


@pytest.fixture
async def test_client() -> AsyncIterator[AsyncTestClient[Litestar]]:
    async with AsyncTestClient(app=app) as client:
        yield client
