from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from dishka.integrations.litestar import setup_dishka
from litestar import Litestar

from src.api.di import container
from src.api.presentations.endpoints import api_router
from src.api.settings import Settings


@asynccontextmanager
async def lifespan(app: Litestar) -> AsyncGenerator[None]:
    yield
    await app.state.dishka_container.close()


def create_app() -> Litestar:
    debug = container.get_sync(Settings).DEBUG
    app = Litestar(
        route_handlers=[api_router], lifespan=[lifespan], debug=debug
    )
    setup_dishka(container, app)
    return app


app = create_app()
