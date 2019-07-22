import os
config = {
    'host': '127.0.0.1',
    'port': 8888
}
ENGINE_PATH = 'mysql+pymysql://root:333333@localhost:3306/boke'
BASE_PATH = os.path.dirname(__file__)
STATIC_PATH = os.path.join(BASE_PATH, 'static')
TEMPLATE_PATH = os.path.join(BASE_PATH, 'template')
password_s = '**'

COOKIE_KEY = 'helloc'
