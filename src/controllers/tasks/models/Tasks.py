from datetime import datetime
from src.controllers import Base
from configs.db import Database
# from sqlalchemy.dialects.postgresql import UUID
from src.services.model_handler import DataHandler
from sqlalchemy import (
    Column,
    Integer,
    DateTime,
    VARCHAR
)


class Tasks(Base, DataHandler):
    __tablename__ = "tasks"
    id = Column(Integer, autoincrement="auto", primary_key=True)
    title = Column(VARCHAR(248), nullable=False)
    description = Column(VARCHAR(248))
    status = Column(VARCHAR(50), nullable=False)
    priority = Column(VARCHAR(50), nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    expires_at = Column(DateTime)
    category = Column(VARCHAR(50))
    
    def get_task_data(self) -> dict:
        return {
            "id": str(self.id),
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "priority": self.priority,
            "created_at": self.datetime_to_str(self.created_at),
            "updated_at": self.datetime_to_str(self.updated_at),
            "expires_at": self.datetime_to_str(self.expires_at),
            "category": self.category,
        }
        
    def datetime_to_str(self, dt):
        return dt.strftime('%d/%m/%Y %H:%M') if dt else None

    # def check_task_expires_at(self):
    #     if datetime.now() > self.expires_at:
    #         return False
    #     return True
    
    def response(self, msg, data):
        return{
            "msg": msg,
            "data": data
        }
    
Base.metadata.create_all(bind=Database().get_engine())