# When we submit a message to 'myapp.cli' logger it will traverse the entire tree of the loggers
# i.e it will also go to 'myapp' logger

# This is because of propagation
import logging
import sys

logger = logging.getLogger(__name__)
stdout = logging.StreamHandler(stream=sys.stdout)
fmt = logging.Formatter("<%(name)s> %(levelname)s %(message)s")
stdout.setFormatter(fmt)
logger.setLevel(logging.DEBUG)  # Log level
logger.addHandler(stdout)

# logger.propagate = False

logger.info("Hello")
