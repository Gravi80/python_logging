import logging
import sys

logger = logging.getLogger(__name__)

stdout = logging.StreamHandler(stream=sys.stdout)
fmt = logging.Formatter("<%(name)s> %(levelname)s %(message)s")
stdout.setFormatter(fmt)
logger.setLevel(logging.DEBUG)  # Log level
logger.addHandler(stdout)
