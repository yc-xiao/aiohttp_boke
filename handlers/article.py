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
        user_id = self.request['user_id']
        if not user_id:
            raise web.HTTPForbidden(text="当前用户未登陆")
        data = await self.request.post()
        if(user_id != data.get("user_id")):
            raise web.HTTPInternalServerError(text="更新失败!")
        title = data.get("title")
        content = data.get("content")
        description = data.get("description")
        article_id = data.get("article_id")
        session = self.request["session"]
        article = session.query(ArticleModel).filter_by(article_id = article_id).first()
        if not article:
            raise web.HTTPInternalServerError(text="文章不存在!")
        article.title = title
        article.description = description
        article.content = content
        session.commit()
        return web.HTTPOk(text="文章更新成功!")

@routes.view('/article/{id}')
class Article(web.View):
    async def get(self):
        article_id = self.request.match_info.get('id')
        session = self.request["session"]
        article = session.query(ArticleModel).filter_by(article_id=article_id).first()
        if article:
            return web.json_response(article.toString())
        else:
            return web.HTTPInternalServerError(text="文章不存在!")

    async def delete(self):
        article_id = self.request.match_info.get('id')
        session = self.request["session"]
        article = session.query(ArticleModel).filter_by(article_id=article_id).delete()
        session.commit()
        return web.HTTPOk(text="文章删除成功!")
