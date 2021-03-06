from pyramid.config import Configurator

from .models.node import root_factory


def main(global_config, **settings):
    config = Configurator(settings=settings,
                          root_factory=root_factory)
    config.include('pyramid_tm')
    config.include('pyramid_sqlalchemy')
    config.include('pyramid_jinja2')

    config.add_static_view('static', 'moonbase:static')
    config.add_static_view('deform_static', 'deform:static')

    config.scan('.views')

    return config.make_wsgi_app()
