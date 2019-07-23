from aiohttp_jinja2 import template
from .base import routes

@routes.get('/')
@template('index.html')
async def index(request):
    pass

@routes.get('/u/{id}')
@template('user.html')
async def index(request):
    pass

@routes.get('/a/{id}')
@template('write.html')
async def index(request):
    pass
