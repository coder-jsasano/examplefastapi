import logging
import logging.config
#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                    datefmt='%m/%d/%Y %H:%M:%S')

#import Logging_helper


#logging.debug("This is a debug message")
#logging.info("This is a info message")
#logging.warning("This is a warning message")
#logging.error("This is a error message")
#logging.critical("This is a critical message")

#logger = logging.getLogger(__name__)

#Create handler
#stream_h = logging.StreamHandler()
#file_h = logging.FileHandler('file.log')

#Level and the format
#stream_h.setLevel(logging.WARNING)
#file_h.setLevel(logging.ERROR)

#formatter= logging.Formatter('%(name)s - %(levelname)s - %(message)s')
#stream_h.setFormatter(formatter)
#file_h.setFormatter(formatter)

#logger.addHandler(stream_h)
#logger.addHandler(file_h)

#logger.warning('This is a warning')
#logger.error('This is an error')


#logging.config.fileConfig('Logging.conf')

#logger = logging.getLogger('simpleExample')
#logger.debug("This is a debug message")

#import traceback

#try:
#    a = [1,2,3]
#    val = a[4]
#except IndexError as e:
#    logging.error(e, exc_info=True)
#except:
#    logging.error("The error is %s", traceback.format_exc())

from logging.handlers import RotatingFileHandler
from logging.handlers import TimedRotatingFileHandler
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#roll over after 2KB and keep backup logs, app.log.1, app.log.2, etc
handler = RotatingFileHandler("app.log", maxBytes=2000, backupCount=5)
logger.addHandler(handler)

# s, m, h, d, midnight, w0=Mon, w1=Tue
#handler = TimedRotatingFileHandler("timed_test.log", when='s', interval=5, backupCount=5)
#logger.addHandler(handler)

for _ in range(10000):
    logger.info("Hello World")
  





