from datetime import datetime
from logging.handlers import TimedRotatingFileHandler
from os import mkdir, path
from time import gmtime
import logging as log

def configure(filename):
    _create_log_folder()
    
    logger = log.getLogger()
    logger.setLevel(log.DEBUG)
    
    date_format = "%d-%m-%Y"
    log_dir = f"log/{filename}.log"
    
    console_handler = log.StreamHandler()
    file_handler = TimedRotatingFileHandler(
        log_dir,
        when="midnight",
        interval=1,
        utc=True,
        backupCount=9
    )
    
    formatter = log.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s",
        date_format + " %H:%M:%S",
    )
    formatter.converter = gmtime
    
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    
    logger.handlers = []
    
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
def _create_log_folder():
    folder_name = "log"
    if not path.exists(folder_name):
        mkdir(folder_name)
