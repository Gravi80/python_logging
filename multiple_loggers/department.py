import logging
import sys

format = "%(asctime)s %(levelname)-8s <%(name)s> %(department_name)s"
level = 10

# Creates if doesn't exists
logger = logging.getLogger(__name__)  # when this script is executed directly __name__ = '__main__'
# and when executed from an import  __name__ = 'multiple_loggers.employee'

# configure logger
logger.setLevel(level)
formatter = logging.Formatter(format, datefmt="%Y-%m-%d %H:%M:%S")

stream_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler('multiple_loggers/logs/department.log')

file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


class Department:
    def __init__(self, name, epmloyees):
        self._name = name
        self._employees = epmloyees

        logger.info('Created Department:', extra={'department_name': self._name})
