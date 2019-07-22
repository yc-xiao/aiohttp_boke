from handlers.base import routes, BaseRequest
from setting import STATIC_PATH, TEMPLATE_PATH, BASE_PATH
from importlib import import_module
import aiohttp_jinja2
import jinja2
import os


def set_routes(app):
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(TEMPLATE_PATH))
    set_route(app)
    app.add_routes(routes)
    app.router.add_static('/static', STATIC_PATH)
    app.router.add_static('/', TEMPLATE_PATH)


def set_route(app):
    def add_handler(mod):
        module_path = mod.__path__[0]
        module_name = mod.__name__
        for file in os.listdir(module_path):
            file_name = os.path.join(module_path, file)
            if os.path.isdir(file_name) and '__init__.py' in os.listdir(file_name):
                nmod = import_module('.'.join([module_name, file]))
                add_handler(nmod)
            elif file.endswith('.py') and file != '__init__.py':
                nmod = import_module('.'.join([module_name, file[:-3]]))
                for c in nmod.__dict__.values():
                    if not isinstance(c, BaseRequest):
                        continue
                    path = c.__path__
                    method = c.__method__
                    app.router.add_route(method, path, c.go)
    mod = import_module('handlers')
    add_handler(mod)
