import logging as log
from aiohttp import web
from src.controllers.tasks.models.Tasks import Tasks
from datetime import datetime, timedelta


class TaskController:
    async def get_tasks(self, request):
        try:
            tasks_db = Tasks.all()

            data = []

            for task in tasks_db['data']:
                task_data = task.get_task_data()
                data.append(task_data)
                
            result = {
                'data': data,
            }
            return web.json_response(result)

        except Exception as ex:
            log.error(f"Error: {ex}")
            raise web.HTTPBadRequest(text=str(ex))
        finally:
            if 'tasks_db' in locals():
                tasks_db['session'].close()
                
    async def create_task(self, request):
        try:
            payload = await request.json() if request.has_body else {}
            title = payload.get('title', False)
            description = payload.get('description', False)
            status = payload.get('status', False)
            priority = payload.get('priority', False)
            expires_at = payload.get('expires_at', False)
            category = payload.get('category', False)
            
            if not title:
                raise ValueError(text="Task title not found")

            if not description:
                raise ValueError(text="Task description not found")
            
            if not status:
                raise ValueError(text="Task status not found")
            
            if not priority:
                raise ValueError(text="Task priority not found")
            
            if not expires_at:
                raise ValueError(text="Task expires_at not found")

            if not category:
                raise ValueError(text="Task category not found")
            
            new_task = Tasks(
                title=title,
                description=description,
                status=status,
                priority=priority,
                created_at=datetime.now(),
                updated_at=datetime.now(),
                expires_at=datetime.now() + timedelta(days=expires_at),
                category=category
            )
            
            created = new_task.create()
            
            if not created:
                raise ValueError("Error to create Task")
            
            data = {
                "id": str(new_task.id),
                "title": new_task.title,
                "status": new_task.status
            }
            
            return web.json_response(
                status=201,
                data=new_task.response("Task created successfully!", data)
            )
            
        except Exception as e:
            return web.HTTPBadRequest(text=str(e))
            
    async def update_task(self, request):
        try:
            task_id = request.match_info.get("id")
            payload = await request.json() if request.has_body else {}

            task_db = Tasks.by_id(task_id)
            task = task_db["data"]
            new_status = payload.get('status')
            task.status = new_status
            task.updated_at = datetime.now()
            updated = task.update()

            if not updated:
                raise ValueError("Error to update task")
            
            data = {
                "id" : str(task.id),
                "status" : task.status
            }

            return web.json_response(data)
        
        except Exception as e:
            return web.HTTPBadRequest(text=str(e))
        
        finally:
            if "task_db" in locals():
                task_db["session"].close()

    async def delete_task(self, request):
        try: 
            recept_id = request.match_info.get("id")
            task_db = Tasks.by_id(recept_id)

            if not task_db:
                return web.HTTPBadRequest(text = "Task not found")

            task = task_db["data"]
            deleted = task.delete()

            if not deleted:
                return web.HTTPBadRequest(text = "Error to delete your task")

            data = {
                "text": "Task deleted",
            }

            return web.json_response(data)

        except Exception as e:
            return web.HTTPBadRequest(text=str(e))

        finally:
            if "task_db" in locals():
                task_db["session"].close() 