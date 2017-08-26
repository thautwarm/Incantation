#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 15:36:27 2017

@author: misakawa
"""

    

class Chain(object):
    def __init__(self, inst):
        self.inst = inst
    def __getattribute__(self, attr):
        if attr in globals():
            def _f(*args, **kwargs):
                return globals()[attr](self.inst, *args, **kwargs)
            return _f
        else:
            return super(Chain, self).__getattribute__(attr)
        
def to_chain(cls):
    class newclass(cls):
        @property
        def chain(self):
           return Chain(self)
    def init(*args, **kwargs):
        return newclass(*args, **kwargs)
    return init

a = to_chain(list)([1,2,3])

def add(self, x): return self+x
a.chain.add([1,2,3])