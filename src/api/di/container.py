from dishka import make_async_container

from .providers import (
    AppAlchemyProvider,
    LogsAlchemyProvider,
    settings_provider,
)

container = make_async_container(
    AppAlchemyProvider(),
    LogsAlchemyProvider(),
    settings_provider,
)
