from .base import aroute, BaseRequest
from aiohttp import web

@aroute('/article/{func}/')
class Ariticle(BaseRequest):
    async def go(self, request):
        return web.json_response({}})

ariticle = Ariticle()
