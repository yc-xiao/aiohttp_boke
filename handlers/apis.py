from .base import BaseRequest, aroute
from model import UserModel, md5
from others import get_token
from aiohttp import web
from others import tokens


@aroute('/api/{func}', method='*')
class Api(BaseRequest):
    mapping = {
        'login':'login',
        'back':'back',
    }
    async def go(self, request):
        if request.method == 'GET':
            data = request.query_string
            if data:
                data = {k:v for k,v in [_.split('=') for _ in data.split('&')]}
        elif request.method == 'POST':
            data = await request.post()
            data = {k:v for k,v in data.items()}
        func = request.match_info.get('func')
        results = await getattr(self, func)(request, data)
        # results = results if results else {}
        # print(results)
        if isinstance(results, dict):
            return web.json_response(results)
        return results

    async def login(self, request, data):
        name = data.get('name')
        password = data.get('password')
        session = request.get('session')
        user = session.query(UserModel).filter_by(name=name, password=md5(password)).first()
        if user:
            response = web.json_response(user.toString())
            response.set_cookie('token', get_token(user.user_id))
            return response
        else:
            raise web.HTTPInternalServerError(text='登陆失败，账号或密码错误')

    async def back(self, request, data):
        if request['token'] in tokens:
            tokens.pop(request['token'])
        return {}


api = Api()
