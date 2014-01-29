from pyramid.paster import get_app, setup_logging
import sys

sys.path.insert(0, '/www/td-odin/tdodin')

ini_path = '/www/td-odin/development.ini'
setup_logging(ini_path)
application = get_app(ini_path, 'main')
