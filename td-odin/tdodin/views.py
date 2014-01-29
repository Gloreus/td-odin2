from pyramid.view import view_config
import data

@view_config(route_name='home', renderer='home.jinja2', layout='base')
def my_view(request):
    return {'content_name': 'content/tdodin.html'}

@view_config(route_name='st_content', renderer='home.jinja2',  layout='base')
def st_content_view(request):
    return {'content_name': 'content/%(name)s.html' % request.matchdict}
