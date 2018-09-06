import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# Limits maximum Size of a logfile
handler = RotatingFileHandler('handlers/logs/rotating.log', maxBytes=20, backupCount=5)
fmt = logging.Formatter("%(levelname)s %(message)s")
handler.setFormatter(fmt)
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)

# The handler’s level is set to WARNING,
# so all events at this and greater severities will be output.
logger.info("Info message")
