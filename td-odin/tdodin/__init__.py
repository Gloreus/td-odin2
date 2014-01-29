from pyramid.config import Configurator

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('st_content', '/st_content/{name}')
    config.scan('.layouts')
    config.scan('.panels')
    config.scan('.views')
    app =  config.make_wsgi_app()
    return app

