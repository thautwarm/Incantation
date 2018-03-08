from collections import Iterable
from .err import ArgumentError
from cytoolz import curry
from functools import update_wrapper


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


def info(incatation_object, return_str=False, print_info=True):
    if not hasattr(incatation_object, 'help'):
        raise ArgumentError('Require an incantation objject.')

    doc = incatation_object.help()
    if print_info:
        print(doc)
    if return_str:
        return doc


def doc_printer(func):
    def wrap(*args, **kwargs):
        doc = f'{func.__qualname__}: \n {func.__doc__}'
        if 'no_print' in kwargs or 'no_print' in args:
            return doc
        print(doc)
        return doc

    return wrap


class ClassProperty:
    def __init__(self, method):
        self.method = method

    def __get__(self, object, instance_cls):
        return self.method(instance_cls)


def default_initializer(init):
    def wrap(self, *args, **kwargs):
        if args and args[0] is super:
            mro = self.__class__.mro()
            mro[mro.index(self.__class__) + 1].__init__(self, super)
            return

        init(self, *args, **kwargs)

    update_wrapper(wrap, init)
    return wrap


def call_func(func):
    return func()
