from pyramid_layout.layout import layout_config


@layout_config(name='base', template='templates/layouts/layout.jinja2')

class AppLayout(object):

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.home_url = request.application_url

    @property
    def project_title(self):
        return 'td-odin.ru'

    def add_heading(self, name, *args, **kw):
        self.headings.append((name, args, kw))
