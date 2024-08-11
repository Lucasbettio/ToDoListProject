from sqlalchemy.orm import Session
from configs.db import Database

db = Database()

class DataHandler:

    @classmethod
    def all(self):
        session = db.get_session()
        query = session.query(self)
        query = query.all()
        
        return_data = {
            "data": query,
            "session": session,
        }
        
        return return_data
    
    @classmethod
    def by_id(self, id):
        session = db.get_session()
        query = session.query(self)
        query = query.filter_by(id=id).first()
        
        return_data = {
            "data": query,
            "session": session
        }

        return return_data

    def create(self) -> bool:
        try:
            session = db.get_session()
            session.add(self)
            session.commit()
            return True
        except Exception as e:
            print(str(e))
            return False

    def update(self):
        try:
            session = Session.object_session(self)
            session.commit()
            return self

        except Exception as e:
            print(str(e))
            return False
    
    def delete(self):
        try:
            session = Session.object_session(self)
            session.delete(self)
            session.commit()

        except Exception as e:
            print(str(e))
            return False
    
    @classmethod
    def get_session(self):
        return db.get_session()