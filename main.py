from others import logging, log_handler, _on_startup, _on_shutdown
from routes import set_routes
from setting import config
from aiohttp import web
import asyncio


def init():
    logging.info('statr server in {host}:{port}'.format(**config))
    app = web.Application(middlewares=[log_handler,])
    set_routes(app)
    app.on_startup.append(_on_startup)
    app.on_shutdown.append(_on_shutdown)
    web.run_app(app, **config, access_log=None)
    #return app

async def main():
    logging.info('statr server in {host}:{port}'.format(**config))
    runner = web.AppRunner(init())
    await runner.setup()
    site = web.TCPSite(runner, host='0.0.0.0', port=2333)
    await site.start()

if __name__ == "__main__":
    init()


    '''
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        pass
    loop.close()
    '''
