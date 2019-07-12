from .base import BaseRequest, aroute
from aiohttp import web


@aroute('/api/{func}/', method='*')
class Api(BaseRequest):
    mapping = {
        "get_user_all": "get_user_all"
    }
    async def go(self, request):
        #func = request.match_info.get('func', 'get_user_all')
        #getattr(self, func)()
        if request.method == "GET":
            args = request.query_string
        elif request.method == "POST":
            args = await request.post()
        print(args)
        return web.json_response({}})
        
    async def get_user_all(self):
        pass
api = Api()
