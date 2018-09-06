import logging
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Limits the amount of TIME a log will stick around
# This file rotates every 2 days with 5 backup logs
handler = TimedRotatingFileHandler('handlers/logs/time_rotating.log', when="d", interval=2, backupCount=5)
fmt = logging.Formatter("%(levelname)s %(message)s")
handler.setFormatter(fmt)
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)

# The handler’s level is set to WARNING,
# so all events at this and greater severities will be output.
logger.info("Info message")
