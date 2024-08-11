import os
from configs.settings import settings as db_info
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Database:
    def __init__(self):
        self.__engine = create_engine(
            get_conn_str(db_info),
            pool_size=db_info.DB_POOL_SIZE,
            max_overflow=db_info.DB_POOL_OVERFLOW,
        )
        self.__Session = sessionmaker(bind=self.__engine, autocommit=False)
        
    def get_engine(self):
        return self.__engine
    
    def get_session(self):
        self.__session = self.__Session()
        return self.__session
    
def get_conn_str(db) -> str:
    conn = f"{db.DB_DIALECT}://{db.DB_USER}:{db.DB_PWD}@{db.DB_HOST}:{db.DB_PORT}/{db.DB_NAME}"
    return conn
