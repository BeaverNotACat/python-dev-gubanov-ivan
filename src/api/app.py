from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from dishka.integrations.litestar import setup_dishka
from litestar import Litestar

from src.api.di import container
from src.api.presentations.endpoints import api_router


@asynccontextmanager
async def lifespan(app: Litestar) -> AsyncGenerator[None]:
    yield
    await app.state.dishka_container.close()


app = Litestar(route_handlers=[api_router], lifespan=[lifespan])
setup_dishka(container, app)
