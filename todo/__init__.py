from pyramid.config import Configurator
from pyramid_sqlalchemy import metadata


def main(global_config, **settings):
    config = Configurator(settings=settings,
                          root_factory='.resources.Root')
    config.include('pyramid_jinja2')
    config.include('.security')
    config.scan('.todos')

    config.include('pyramid_sqlalchemy')
    metadata.create_all()

    config.add_static_view('static', 'todo:static')
    config.add_static_view('deform_static', 'deform:static')
    config.add_route('list', '/')
    config.add_route('add', '/add')
    config.add_route('view', '/{id}/view')
    config.add_route('edit', '/{id}/edit')
    config.add_route('delete', '/{id}/delete')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    return config.make_wsgi_app()
