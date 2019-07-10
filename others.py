from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from aiohttp.web import middleware
from functools import wraps
from setting import ENGINE_PATH
import logging
logging.basicConfig(level=logging.INFO)

"""
    信号：应用初始化和结束 _on_startup, _on_shutdown
    中间件: 请求处理
"""


@middleware
async def log_handler(request, handler):
    logging.info('start in middlerware')
    response = await handler(request)
    logging.info('end out middlerware')
    return response

async def _on_startup(app):
    temp_app = app
    logging.info('start signals server')
    logging.info('start init server')
    init(app)


async def _on_shutdown(app):
    logging.info('stop signals server')
    logging.info('stop connection server')
    close(app)

def init(app):
    global engine, Session
    engine = create_engine(ENGINE_PATH)
    Session = sessionmaker(bind=engine)
    print(engine, Session)

def close(app):
    pass
