from sqlalchemy.exc import IntegrityError
from aiohttp import web
from aiohttp_jinja2 import template
from model import UserModel, get_unit_id, md5
from .base import routes

@routes.get('/')
@template('index.html')
async def index(request):
    return

@routes.get('/u/{id}')
@template('user.html')
async def index(request):
    uuser_id = request.match_info.get('id')
    return response

@routes.view('/user/')
class User(web.View):
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
        user_id = self.request.match_info.get('id')
        session = self.request['session']
        user = session.query(UserModel).filter_by(user_id=user_id).first()
        if not user:
            return web.HTTPInternalServerError(text="用户不存在!")
        return web.json_response(user.toString())

    async def delete(self):
        print('delete')
        return web.Response(text = 'index1')
