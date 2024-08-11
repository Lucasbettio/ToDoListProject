from aiohttp import web
from src.routes.Tasks import tasks_routes


class App:
    def __init__(self):
        self.app = web.Application()
        self.prefix = '/api'
        self.routes()
    
    async def _status(self):
        return web.Response(text="Healthy and working")

    def routes(self):
        self.app.add_routes([web.get(f"{self.prefix}/status", self._status)])
        self.app.add_routes(tasks_routes(self.prefix))
    
    def get_app(self):
        return self.app