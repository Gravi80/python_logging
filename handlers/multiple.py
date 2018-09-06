import logging
import sys

logger = logging.getLogger(__name__)

stdout = logging.StreamHandler(stream=sys.stdout)
errfile = logging.FileHandler(filename='handlers/logs/error.log')

fmt = logging.Formatter("%(levelname)s %(message)s")
stdout.setFormatter(fmt)
errfile.setFormatter(fmt)

errfile.setLevel(logging.ERROR)  # Handler level > Parent level
logger.setLevel(logging.DEBUG)  # Parent level

logger.addHandler(stdout)
logger.addHandler(errfile)

logger.info("Info message")
logger.error("Error message")

# python handlers/multiple.py
