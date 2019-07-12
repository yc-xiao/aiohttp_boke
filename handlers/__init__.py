"""
from .apis import *
from .user import *
from .base import BaseRequest, routes

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
