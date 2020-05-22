from os import path
from os import getcwd
import logging


def _base_paths():
    home = path.expanduser('~')
    pwd = getcwd()
    yield path.join(pwd, 'etc')
    yield pwd
    yield path.join(home, 'etc') 
    yield home 


def cfg_lookup(filename : str):
    all_paths = list(_base_paths())
    for cfg_path in all_paths:
        if path.exists(path.join(cfg_path, filename)):
            return path.join(cfg_path, filename)
    logging.error(f'{filename} does not exist in: {all_paths}')
