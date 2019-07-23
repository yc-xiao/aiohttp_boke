from setting import ENGINE_PATH, COOKIE_KEY

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from aiohttp.web import middleware
from time import time
from random import randint

import hashlib
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
    token = request.cookies.get('token')
    request['user_id'] = token_user(token)
    request['session'] = Session()
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
        return
    return result[0]

tokens = {}
def u_token(key, user_id):
    return hashlib.md5((key + user_id + COOKIE_KEY).encode()).hexdigest()

def user_token(user_id, expires=3600):
    # user_id-key-token-expires
    key = str(randint(1000,9999))
    expires = str(expires + int(time()))
    token = u_token(key, user_id)
    tokens[user_id] = '_'.join([user_id, key, token, expires])
    return tokens[user_id]

def token_user(token):
    if not token:
        return
    ts = token.split('_')
    _token = tokens.get(ts[0])
    if _token and len(ts) == 4 and ts[2] == u_token(ts[1], ts[0]) and  time() - int(ts[-1]) < 0:
            return ts[0]
    tokens.pop(ts[0], None)
