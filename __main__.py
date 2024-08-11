from aiohttp import web
from src.App import App
from config import settings


app = App()

if __name__ == "__main__":
    web.run_app(
        app.get_app(),
        host=settings.API_HOST,
        port=settings.API_PORT
    )