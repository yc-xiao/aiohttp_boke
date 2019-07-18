from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from aiohttp.web import middleware
from time import time

from setting import ENGINE_PATH, COOKIE_KEY
import logging
logging.basicConfig(level=logging.INFO)

"""
    信号：应用初始化和结束 _on_startup, _on_shutdown
    中间件: 请求处理
"""
tokens = {}



@middleware
async def log_handler(request, handler):
    logging.info('start in middlerware')
    logging.info(str(request.url))
    request['session'] = Session()
    token = request.cookies.get('token', False)
    request['user_id'] = to_token(token)
    request['token'] = token
    response = await handler(request)
    request['session'].close()
    logging.info('end out middlerware')
    return response

async def _on_startup(app):
    logging.info('start signals server')
    logging.info('start init server')
    init(app)


async def _on_shutdown(app):
    logging.info('stop signals server')
    logging.info('stop connection server')
    close(app)

def init(app):
    global engine, Session
    app["tokens"] = tokens
    engine = create_engine(ENGINE_PATH)
    Session = sessionmaker(bind=engine)

def close(app):
    pass

def get_token(user_id, expires=3600):
    expires = expires + int(time())
    token = "-".join([user_id, str(expires), COOKIE_KEY])
    tokens[token] = True
    return token

def to_token(token):
    _token = tokens.get(token, False)
    if not _token:
        return
    result = token.split('-')
    if time() - int(result[1]) > 0:
        tokens.pop(token)
        return
    return result[0]
