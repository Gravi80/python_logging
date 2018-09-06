import myapp.api
import myapp.cli

print("You are seeing duplicate message because "
      "messages logged in 'myapp.api' and 'myapp.cli' are also being propagated to "
      "the handler present in 'myapp' logger. Therefore all handlers should be defined only "
      "in the base module/logger i.e 'myapp.__init__.py'")
print("You can also disable propagation")

# python hierarchy/main.py

# myapp.api -> logging.NOTSET
# myapp ->     logging.DEBUG
#       If child log level is NOTSET then Parent log level will be propagated to child
