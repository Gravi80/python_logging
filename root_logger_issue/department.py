import logging

format = "%(asctime)s %(levelname)-8s <%(name)s> %(department_name)s"
level = 10

logging.basicConfig(format=format, level=level, datefmt="%Y-%m-%d %H:%M:%S")


class Department:
    def __init__(self, name, epmloyees):
        self._name = name
        self._employees = epmloyees

        logging.info('Created Department:', extra={'department_name': self._name})
