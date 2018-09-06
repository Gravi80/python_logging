# 1). Available on both Handlers and loggers
# 2). Creation of more sophisticated logging rules
#       Ex-     DEBUG, INFO  => in stdout
#               WARN, ERROR, CRITICAL => in stderror
#     Without filters you can't achieve this bcz stdout will include WARN, ERROR, CRITICAL also
#     because of high log level
# 3). Can manipulate log record since they receive entire record

# Drop everything except info messages
def info_filter(record):
    return record.levelname == 'INFO'


import logging


class ContextFilter(logging.Filter):
    def filter(self, record):
        record.name = "new name"
        record.some_param = "some_param"
        return True


handler = logging.StreamHandler()
handler.formatter = logging.Formatter("%(some_param)s %(name)s %(message)s")
handler.addFilter(ContextFilter())
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

logger.info("ContextFilter")


# Drop everything except info messages
class InfoFilter(logging.Filter):
    def filter(self, record):
        return record.levelname == 'INFO'


handler = logging.StreamHandler()
handler.formatter = logging.Formatter("%(some_param)s %(name)s %(message)s")
handler.addFilter(InfoFilter())
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

logger.debug("InfoFilter")
