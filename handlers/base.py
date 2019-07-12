"""
    通过BaseRequest和aroute实现路由加载
    例子:
    @aroute('/api/{func}/')
    class Api(BaseRequest):
        async def go(self, request):
            入口函数
"""

from aiohttp import web
routes = web.RouteTableDef()


class BaseRequest(object):
    def __init__(self):
        pass
    async def go(self, request):
        mapping = {}

def aroute(path, method='get'):
    def inner(C):
        C.__path__ = path
        C.__method__ = method
        return C
    return inner
