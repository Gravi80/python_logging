[Hierarchy] Specify your base logger name in documentation when using \_\_name\_\_ as logger name.

1. logging_example.py
2. root_logger_issue/main.py
3. multiple_loggers/main.py
4. log_exception_stacktrace/main.py
4. handlers/*.py
5. custom_formatter.py
6. hierarchy/main.py
7. filters.py
8. logging_config/main.py

## Logger
Receives log messages
* level
* propagate
* filters
* handlers

## LogRecord
Contain information about the function, file name, full path where the log was requested,
the string that was passed, arguments, call stack information, etc.
These are the objects that are being logged. Every time we invoke our loggers, we are creating instances of these objects.

* Created automatically by the logger every time something is logged
* Can be created manually via logging.makeLogRecord

## Handlers
https://docs.python.org/2/library/logging.handlers.html#module-logging.handlers

Handlers emit the log records into any output. They take log records and handle them in the function of what they were built for.
As an example, a FileHandler will take a log record and append it to a file.

 The handler will then use a Formatter to turn the LogRecord into a string and emit that string.

* class
* level
* filters
* formatter

## Formatter
Format a log record for output.
Formatters are in charge of serializing the metadata-rich LogRecord into a string.
There is a default formatter if none is provided.

* format
* date format
* style (%,{,$)

## Filters
Control which LogRecord should be emitted

1. from Logger ---> Handlers    [Filter at logger level]
2. from Handlers ---> Formatter    [Filter at Handler level]

Users can declare their own filters as objects using a filter <b>method</b> that takes a record as input and returns True/False as output.


### <u style="color: black">References</u>
* https://www.youtube.com/watch?v=apLoTRE1B8c
* https://www.youtube.com/watch?v=jxmzY9soFXg
* https://www.youtube.com/watch?v=24_4WWkSmNo
* https://www.youtube.com/watch?v=DxZ5WEo4hvU
* https://opensource.com/article/17/9/python-logging
* https://www.youtube.com/watch?v=QQzw5f4coSU