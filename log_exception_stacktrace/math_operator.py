import logging

formatter = logging.Formatter(fmt="%(asctime)s %(levelname)-8s <%(name)s> %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler('log_exception_stacktrace/stack_trace.log')

logger = logging.getLogger(__name__)
logger.setLevel(10)

stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        logger.exception('Tried by zero!')
    else:
        return result
