from dishka import make_async_container

from .providers import (
    AppAlchemyProvider,
    LogsAlchemyProvider,
    interactors_provider,
    repositories_provider,
    settings_provider,
)

container = make_async_container(
    AppAlchemyProvider(),
    LogsAlchemyProvider(),
    interactors_provider,
    repositories_provider,
    settings_provider,
)
