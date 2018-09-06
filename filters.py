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
logging.Filter()