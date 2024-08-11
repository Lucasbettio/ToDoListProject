from aiohttp import web
from src.controllers.tasks.tasks_controller import TaskController

task_controller = TaskController()

async def _status():
    return web.Response(text="Tasks healthy and working")

def tasks_routes(prefix):
    return[
        web.get(prefix + '/tasks', task_controller.get_tasks),
        web.post(prefix + '/task', task_controller.create_task)
    ]