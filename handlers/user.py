from sqlalchemy.exc import IntegrityError
from aiohttp_jinja2 import render_template
from aiohttp import web

from model import UserModel, get_unit_id, md5
from .base import routes

@routes.get('/')
async def index(request):
    return web.HTTPFound(location='index.html')

@routes.view('/user/')
class User(web.View):
    async def get(self):
        print('find all')
        return web.Response(text = 'index1')

    async def post(self):
        print('create user')
        data = await self.request.post()
        user_id = get_unit_id()
        name = data.get("name")
        password = data.get("password")
        session = self.request["session"]
        new_user = UserModel(user_id=user_id, name=name, password=md5(password))
        try:
            session.add(new_user)
            session.commit()
        except IntegrityError:
            """
                web.json_response({"name":"helloc"})
                status(int) ==> 请求状态
                body(str) or text(str) or data(dict) ==> 返回body
            """
            return web.HTTPInternalServerError(text="注册失败，用户可能存在")
        return web.Response(text="注册成功")

    async def put(self):
        pdb.set_trace()
        print('修改一条数据')
        data = await self.request.post()
        return web.Response(text = 'index1')
        #    return web.json_response({"name":"helloc"})

@routes.view('/user/{id}')
class User(web.View):
    async def get(self):
        userid = self.request.match_info.get('id')
        return web.json_response(results.toString())

    async def delete(self):
        print('delete')
        return web.Response(text = 'index1')
