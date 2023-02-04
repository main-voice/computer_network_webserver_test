from pyramid.config import Configurator
from pyramid.response import Response


def hello_world(request):
    return Response(
        'Hello world from Pyramid! (url is /hello)\n',
        content_type='text/plain',
    )


def hello_pen(request):
    return Response(
        'Hello world from Pyramid! (url is /pen)\n',
        content_type='text/plain',
    )


config = Configurator()
config.add_route('hello', '/hello')
config.add_route('pen', '/pen')
config.add_view(hello_world, route_name='hello')
config.add_view(hello_pen, route_name='pen')
app = config.make_wsgi_app()
