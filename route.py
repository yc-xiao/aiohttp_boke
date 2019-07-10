from views import routes
from setting import STATIC_PATH

def set_routes(app):
    app.add_routes(routes)
    app.router.add_static('/', STATIC_PATH)
