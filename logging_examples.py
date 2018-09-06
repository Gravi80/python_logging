import logging

LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL}

# https://docs.python.org/3/library/logging.html#logrecord-attributes
format = "%(clientip)s %(asctime)s %(levelname)-8s <%(name)s> %(message)s"
level = LEVELS.get('debug', logging.NOTSET)

logging.basicConfig(format=format, level=level, datefmt="%Y-%m-%d %H:%M:%S")

extra_args = {'clientip': 'localhost'}
logging.info(
    "Since we are using root logger. "
    "Its better to log things with specific loggers because they can be configured separately",
    extra=extra_args)

logging.warning("Warning", extra=extra_args)
logging.error("This is an error", extra=extra_args)
logging.info("String interpolation with '%s'", 'param1', extra=extra_args, stack_info=True)

# Add custom log level
logging.addLevelName(60, 'CUSTOM_LEVEL')
print(logging.getLevelName('ERROR'))
print(logging.getLevelName('CUSTOM_LEVEL'))
logging.log(60, "custom message", extra=extra_args)
