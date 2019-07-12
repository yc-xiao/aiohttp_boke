from aiohttp_jinja2 import render_template
from aiohttp import web

from model import UserModel, get_unit_id
from .base import routes

@routes.get('/')
async def index(request):
    return web.HTTPFound(location='index.html')

@routes.post('/login/')
async def login(request):
    data = await request.post()
    import pdb;pdb.set_trace()
    name = data.get("name")
    password = data.get("password")
    session = request["session"]
    user = session.query(UserModel).filter_by(name=name, password=password).first()
    if not user:
        msg = {"status":"error"}
    else:
        msg = {"status":user.toString()}
    response = web.json_response(msg)
    return response
    # return web.HTTPFound(location='/index.html')

@routes.view('/user/')
class User(web.View):
    async def get(self):
        print('find all')
        return web.Response(text = 'index1')

    async def post(self):
        print('create user')
        data = await self.request.post()
        userid = get_unit_id()
        name = data.get("name")
        password = data.get("password")
        session = self.request["session"]
        new_user = UserModel(userid=userid, name=name, password=password)
        session.add(new_user)
        session.commit()
        return web.HTTPFound(location='/index.html')

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
