import logging
from logging.handlers import RotatingFileHandler
import datetime


def log():

    """Generador de logs para el microservicio

    Returns:
        function: logging
    """  
    now = datetime.datetime.now()
    format_logger = now.strftime('%Y-%m-%d')
    logger = logging.getLogger('')
    logger.setLevel(logging.NOTSET)
    rthandler = RotatingFileHandler(f'''logs/kuantaz-ms-{format_logger}.log''', maxBytes=2 * 1024 * 1024, backupCount=5)
    
    formatter = logging.Formatter('%(asctime)s %(levelname)s | %(message)s')
    rthandler.setFormatter(formatter)

    if(logger.hasHandlers()):
        logger.handlers.clear()

    logger.addHandler(rthandler)
    
    return logger