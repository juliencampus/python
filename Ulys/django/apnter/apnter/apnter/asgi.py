"""
ASGI config for apnter project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""
import asyncio
import os

from django.core.asgi import get_asgi_application
from .websockets import websocket_application, listen_ap, listen, main


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'apnter.settings')

django_application = get_asgi_application()

async def application(scope, receive, send):
    if scope['type'] == 'http':
        await django_application(scope, receive, send)
    elif scope['type'] == 'websocket':
        # asyncio.run(main(scope, receive, send))
        # await websocket_application(scope, receive, send)
        await listen_ap(scope,receive, send)
    else:
        raise NotImplementedError(f"Unknown scope type {scope['type']}")
