from handlers.base import routes, BaseRequest
from setting import STATIC_PATH
from importlib import import_module
import os


def set_routes(app):
    set_route(app)
    app.add_routes(routes)
    app.router.add_static('/', STATIC_PATH)


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


"""
def get_route(app):
    mod = __import__('handlers', locals())
    for c in dir(mod):
        c = getattr(mod, c)
        if type(c) is not type:
            continue
        if c is BaseRequest or not issubclass(c, BaseRequest):
            continue
        path = c.__path__
        method = c.__method__
        app.router.add_route(method, path, c.go)
"""
