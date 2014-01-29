from pyramid_layout.panel import panel_config
import data

@panel_config(
    name='navbar',
    renderer='templates/panels/menu.jinja2'
    )
def navbar(context, request):
    def nav_item(name, url):
        active = request.current_route_url() == url
        item = dict(
            name = name,
            url = url,
            active = active
            )
        return item
	
    nav = [
        nav_item('Mako', request.route_url('home')),
        nav_item('Chameleon', request.route_url('home')),
        nav_item('Jinja2', request.route_url('home'))
        ]
    return {
        'title': 'Demo App',
        'nav': nav
        }

@panel_config(
    name='catalog',
    renderer='templates/panels/mod_catalog.jinja2'
    )
def catalog(context, request):
    return {
        'Tree': data.get_tree()
    }