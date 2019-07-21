import os
config = {
    'host': '0.0.0.0',
    'port': 8888
}
ENGINE_PATH = 'mysql+pymysql://root:333333@localhost:3306/boke'
BASE_PATH = os.path.dirname(__file__)
STATIC_PATH = os.path.join(BASE_PATH, 'static')
password_s = '**'

COOKIE_KEY = 'helloc'
