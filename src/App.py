import aiohttp_cors
from aiohttp import web
from src.routes.Routes import Routes
from src.middlewares.Authentication import Authentication
from src.handlers.Db import check_db_conecction
from logging import log

METHODS = ["GET", "POST", "OPTIONS", "PUT", "REMOVE"]

class App():

    def __init__(self):
        auth = Authentication()
        self.app = web.Application(middlewares=[auth.token_validation])
        self.routes = Routes()
        self._set_routes()
        self.check_app_db_connection()

    def _set_cors(self):
        self.cors = aiohttp_cors.setup(self.app, defaults= {
            "*": aiohttp_cors.ResourceOptions(
                allow_credentials=True,
                expose_headers="*",
                allow_headers="*",
                allow_methods=METHODS,
            )
        })

        for route in list(self.app.router.routes()):
            self.cors.add(route)

    def _set_routes(self):
        self.app.add_routes(self.routes.get_routes())
        self._set_cors()


    def get_app(self):
        return self.app

    def check_app_db_connection(self):
        if check_db_conecction():
            print('==== DB is connected and working! ====')
        else:
            print('==== DB is not connected! ====')