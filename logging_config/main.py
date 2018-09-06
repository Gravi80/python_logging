import logging.config
import yaml
from os import path

with open(path.dirname(__file__) + '/config.yml') as logging_configuration_file:
    config_dict = yaml.load(logging_configuration_file)
    logging.config.dictConfig(config_dict)

import myapp.api
import myapp.cli
