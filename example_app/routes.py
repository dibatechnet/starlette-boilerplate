from starlette.routing import Route, WebSocketRoute

from .views import root
from .sockets import websocket_endpoint


routes = [
    Route('/', root, name='api-root'),
    WebSocketRoute('/ws', websocket_endpoint)
]
