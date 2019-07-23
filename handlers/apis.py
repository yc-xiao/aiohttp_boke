from .base import BaseRequest, aroute
from model import UserModel, ArticleModel, CommentModel, md5
from others import user_token, token_user, tokens
from aiohttp import web


@aroute('/api/{func}', method='*')
class Api(BaseRequest):
    mapping = {
        'login': 'login',
        'back': 'back',
        'articles': 'articles',
        'is_login': 'is_login',
    }

    async def go(self, request):
        if request.method == 'GET':
            data = request.query_string
            if data:
                data = {k: v for k, v in [
                    _.split('=') for _ in data.split('&')]}
        elif request.method == 'POST':
            data = await request.post()
            data = {k: v for k, v in data.items()}
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
        user = session.query(UserModel).filter_by(
            name=name, password=md5(password)).first()
        if user:
            response = web.json_response(user.toString())
            response.set_cookie('token', user_token(user.user_id))
            return response
        else:
            raise web.HTTPInternalServerError(text='登陆失败，账号或密码错误')

    async def back(self, request, data):
        token = request.cookies.get('token')
        if token:
            tokens.pop(token.split('_')[0], None)
        return {}

    async def is_login(self, request, data):
        user = {}
        token = request.cookies.get('token')
        if request['user_id']:
            session = request.get('session')
            user = session.query(UserModel).filter_by(user_id=request['user_id']).first()
        return user if not user else user.toString()

    async def articles(self, request, data):
        nums = int(data.get('nums', 10))
        index = int(data.get('index', -1))
        user_id = data.get('user_id', '')
        title = data.get('title', '')
        art_query = request['session'].query(ArticleModel)
        if title:
            art_query = art_query.filter(
                ArticleModel.title.like("%" + str(title) + "%"))
        if user_id:
            art_query = art_query.filter(ArticleModel.writor_id == user_id)
        if index == -1:
            art_query = art_query.all()
        else:
            art_query = art_query.offset(index * (index + 1)).limit(nums)
        return {each.article_id: each.toString() for each in art_query}


api = Api()
