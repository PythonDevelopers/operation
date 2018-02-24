import os
import yaml

filename = os.path.join(os.path.dirname(__file__), "config.yaml").replace("\\", "/")

config_path = os.path.join(os.path.dirname(__file__), 'config.yaml')

f = open(filename)
y = yaml.load(f)


class Mysql:
        host = y.get('mysql').get('conn').get('host')
        user = y.get('mysql').get('conn').get('user')
        db = y.get('mysql').get('conn').get('database')
        password = y.get('mysql').get('conn').get('password')

