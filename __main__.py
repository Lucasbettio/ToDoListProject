from aiohttp import web
from config import settings
from log_config import configure
from src.App import App

configure("toDoListProject")

app = App()

if __name__ == "__main__":
    web.run_app(
        app.get_app(),
        host=settings.API_HOST,
        port=settings.API_PORT
    )