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
            exec_info=record.exc_info,  # exception info
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

ATTR_TO_JSON = ['name', 'msg', 'args', 'levelname', 'levelno', 'pathname', 'filename', 'module', 'exc_info', 'exc_text',
                'stack_info', 'lineno', 'funcName', 'created', 'msecs', 'relativeCreated', 'thread', 'threadName',
                'processName', 'process']


class JsonFormatter:

    def format(self, record):
        obj = {attr: getattr(record, attr) for attr in ATTR_TO_JSON}
        return json.dumps(obj, indent=4)


handler = logging.StreamHandler()
handler.formatter = JsonFormatter()
logging = logging.getLogger(__name__)
logger.addHandler(handler)
logger.error("Hello")
