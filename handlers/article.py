from sqlalchemy.exc import IntegrityError
from aiohttp import web
from time import time

from model import ArticleModel, get_unit_id, md5
from .base import routes

@routes.view('/article')
class Article(web.View):
    async def post(self):
        print('new article')
        writor_id = self.request['user_id']
        if not writor_id:
            raise web.HTTPForbidden(text="当前用户未登陆")
        data = await self.request.post()
        article_id = get_unit_id()
        title = data.get("title")
        content = data.get("content")
        description = data.get("description")
        writor = data.get("writor")

        session = self.request["session"]
        new_article = ArticleModel(article_id=article_id, writor_id=writor_id, title=title, content=content, description=description, created=str(int(time())),
        writor=writor)
        try:
            session.add(new_article)
            session.commit()
        except IntegrityError:
            return web.HTTPInternalServerError(text="新增失败")
        return web.Response(text="新增成功")

    async def put(self):
        pdb.set_trace()
        print('修改一条数据')
        data = await self.request.post()
        return web.Response(text = 'index1')
        #    return web.json_response({"name":"helloc"})

@routes.view('/article/{id}')
class Article(web.View):
    async def get(self):
        userid = self.request.match_info.get('id')
        return web.json_response(results.toString())

    async def delete(self):
        print('delete')
        return web.Response(text = 'index1')
