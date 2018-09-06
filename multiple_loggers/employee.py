import logging

format = "%(asctime)s %(levelname)-8s <%(name)s> %(email)s %(fullname)s"
logger_level = 10
file_handler_level = 30
stdout_handler_level = 10

# Creates if doesn't exists
logger = logging.getLogger(__name__)  # when this script is executed directly __name__ = '__main__'
# and when executed from an import  __name__ = 'multiple_loggers.employee'

# configure logger
logger.setLevel(logger_level)
formatter = logging.Formatter(format, datefmt="%Y-%m-%d %H:%M:%S")

stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler('multiple_loggers/logs/employee.log')

stream_handler.setLevel(stdout_handler_level)
file_handler.setLevel(file_handler_level)

file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


class Employee:
    def __init__(self, first_name, last_name):
        self._first = first_name
        self._last_name = last_name

        logger.info('Created Employee:', extra={'email': self.email, 'fullname': self.fullname})

    @property
    def email(self):
        return '{}.{}@email.com'.format(self._first, self._last_name)

    @property
    def fullname(self):
        return '{} {}'.format(self._first, self._last_name)
