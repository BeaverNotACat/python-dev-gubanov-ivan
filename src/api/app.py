from litestar import Litestar

from src.api.presentations.endpoints import api_router

app = Litestar(route_handlers=[api_router])
