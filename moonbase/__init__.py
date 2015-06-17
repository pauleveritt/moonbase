from pyramid.config import Configurator

from .models.sqltraversal import root_factory


def main(global_config, **settings):
    config = Configurator(settings=settings,
                          root_factory=root_factory)
    config.include('pyramid_tm')
    config.include('pyramid_sqlalchemy')
    config.include('pyramid_jinja2')

    config.add_static_view('static', 'moonbase:static')
    config.add_static_view('deform_static', 'deform:static')
    config.add_route('home', '/')
    config.add_route('todos_list', '/todos')
    config.add_route('todos_add', '/todos/add')
    config.add_route('todos_view', '/todos/{id}')
    config.add_route('todos_edit', '/todos/{id}/edit')
    config.add_route('todos_delete', '/todos/{id}/delete')

    config.scan('.views')

    return config.make_wsgi_app()
