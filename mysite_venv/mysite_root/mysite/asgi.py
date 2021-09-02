import os
import django

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from .wsgi import *
import chat.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

# 라우팅이란 출발지에서 목적지까지의 경로를 결정하는 기능이다. 사용자가 A 라는 화면에서 B 라는 화면으로 넘어가는 네비게이션을 관리하기 위한 기능을 의미한다.
# Consumer (View에 해당) 으로 연결될 라우팅을 담당하는 부분(django의 url에 해당)

# 클라이언트와 Channels 개발 서버가 연결 될 때, 어느 protocol 타입의 연결인지?
application = ProtocolTypeRouter({
	'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})

'''
This root routing configuration specifies that when a connection is made to the Channels development server,
the ProtocolTypeRouter will first inspect the type of connection.
If it is a WebSocket connection (ws:// or wss://), the connection will be given to the AuthMiddlewareStack.

The AuthMiddlewareStack will populate the connection’s scope with a reference to the currently authenticated user,
similar to how Django’s AuthenticationMiddleware populates the request object of a view function with the currently authenticated user.
(Scopes will be discussed later in this tutorial.)
Then the connection will be given to the URLRouter.

The URLRouter will examine the HTTP path of the connection to route it to a particular consumer, based on the provided url patterns.
Let’s verify that the consumer for the /ws/chat/ROOM_NAME/ path works. Run migrations to apply database changes
(Django’s session framework needs the database) and then start the Channels development server:
'''
