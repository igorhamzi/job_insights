from functools import lru_cache
from csv import DictReader


@lru_cache
def read(path):
    with open(path, 'r') as file:
        dict_reader = DictReader(file)
        list_of_dict = list(dict_reader)

    return list_of_dict
