from dishka import Provider, Scope

from src.api.settings import Settings

settings_provider = Provider(Scope.APP)
settings_provider.provide(lambda: Settings(), provides=Settings)  # noqa: PLW0108 Othervise dishka will try to resolve Settings.__init__ args
