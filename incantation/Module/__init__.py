# -*- coding: utf-8 -*-

from .. import foreach, groupby, andThen, compose, flow_map, flatten, fastmap
from .abst import abstract_object,indent_setter, default_attr
class blockquote(indent_setter, abstract_object):
    """
    See http://materializecss.com/typography.html
    user help : >> help (blockquote.init)
    ------------------------------
        Guide:
           blockquote("Tips here!")
    """
    def init(self, content, **attributes):
        body = \
"""
{{indent}}<blockquote {{attributes_dict}}>
{{indent+Indent_unit}}{{content}}.
{{indent}}</blockquote>
"""
        self.conf.update(dict(content = content, indent = '',  attributes_dict = attributes))
        self.body = body
        