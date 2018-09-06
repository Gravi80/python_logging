import logging

LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL}

# https://docs.python.org/3/library/logging.html#logrecord-attributes
format = "%(clientip)-8s %(asctime)s %(levelname)-8s <%(name)s> %(message)s"
level = LEVELS.get('debug', logging.NOTSET)

logging.basicConfig(format=format, level=level, datefmt="%Y-%m-%d %H:%M:%S")

extra_args = {'clientip': 'localhost'}
logging.info(
    "Since we are using root logger. "
    "Its better to log things with specific loggers because they can be configured separately",
    extra=extra_args)
