from collections import Iterable
from .err import ArgumentError
from cytoolz import curry


@curry
def isa(obj, type):
    return isinstance(obj, type)


def is_unque(collections: Iterable):
    count = set()
    for each in collections:
        if each in count:
            return False
        count.add(each)
    return True


class BiMap:

    def __init__(self, c1: Iterable, c2: Iterable):
        self.to = dict(zip(c1, c2))
        self.back = dict(zip(c2, c1))

    def __getitem__(self, item):
        sign, it = item
        if sign is '>':
            return self.to[it]
        elif sign is '<':
            return self.back[it]
        else:
            raise ArgumentError
