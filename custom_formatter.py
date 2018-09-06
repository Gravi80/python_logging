import logging
import sys
from datetime import datetime
import json


class StructuredLogFormatter(logging.Formatter):
    def format(self, record):
        my_message = dict(
            name=record.name,
            timestamp=str(datetime.now()),
            level=record.levelname,
            message=record.msg,
            exec_info=record.exc_info, # exception info
            pathname=record.pathname,
            lineno=record.lineno
        )
        return json.dumps(my_message)


logger = logging.getLogger(__name__)
stdout = logging.StreamHandler(stream=sys.stdout)

fmt = StructuredLogFormatter()
stdout.setFormatter(fmt)
logger.setLevel(logging.DEBUG)  # Parent level
logger.addHandler(stdout)

logger.info("Info message some")
