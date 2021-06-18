from starlette.applications import Starlette

from .settings import DEBUG
from .routes import routes
from .middleware import middleware
from .handlers import on_startup, on_shutdown

app = Starlette(
    debug=DEBUG,
    routes=routes,
    middleware=middleware,
    on_startup=on_startup,
    on_shutdown=on_shutdown,
)
