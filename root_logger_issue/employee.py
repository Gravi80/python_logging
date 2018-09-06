import logging

format = "%(asctime)s %(levelname)-8s <%(name)s> %(email)s %(fullname)s"
level = 10

logging.basicConfig(format=format, level=level, datefmt="%Y-%m-%d %H:%M:%S")


class Employee:
    def __init__(self, first_name, last_name):
        self._first = first_name
        self._last_name = last_name

        logging.info('Created Employee:', extra={'email': self.email, 'fullname': self.fullname})

    @property
    def email(self):
        return '{}.{}@email.com'.format(self._first, self._last_name)

    @property
    def fullname(self):
        return '{} {}'.format(self._first, self._last_name)
