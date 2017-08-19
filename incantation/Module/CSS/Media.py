# -*- coding: utf-8 -*-
from ..abst import abstract_object,indent_setter, Seq, default_attr

class Img(indent_setter, abstract_object):
    def init(self, content, **attributes):
        pass