#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 20:18:27 2017

@author: misakawa
"""


from ..abst import abstract_object,indent_setter, default_attr, attrset_sugar
from .Icons import mode_edit
class FAB(indent_setter, abstract_object):
    """
    See http://materializecss.com/buttons.html
    user help : >> help (FAB.init)
        Guide:
            from incantation.Module.Component.Icons import icon
            fab = FAB([dict(color = 'red',  icon = icon("insert_chart"),  href = ...),
                       dict(color = 'blue', icon = icon("publish"),       href = ...),
                       ...
                       ], loc = 'relative')
    """
    @default_attr(attr = 'class', value = 'fixed-action-btn')
    def init(self, content, **attributes):
        sugar = attrset_sugar(self.conf, attributes)
        sugar('color', 'red')
        sugar('icon', mode_edit)
        sugar('horizon',  False)
        sugar('loc', "fixed")
        if self.conf['horizon']:
            attributes['class']+=' horizontal'
        body =\
"""
{{indent}}<div {{attributes_dict}} {% if loc != 'fixed' %}style="position: {{loc}};"{% else %} {% endif %}>
{{indent+Indent_unit}}<a class="btn-floating btn-large {{color}}">
{{indent+Indent_unit*2}}<i class="large material-icons">{{icon}}</i>
{{indent+Indent_unit}}</a>
{{indent+Indent_unit}}<ul>
{{indent+Indent_unit}}{% for subicon in content %}
{{indent+Indent_unit*2}}<li><a href="{{subicon.href}}" class="btn-floating {{subicon.color}}">{{subicon.icon}}</a></li>
{{indent+Indent_unit}}{% endfor %}
{{indent+Indent_unit}}</ul>
{{indent}}</div>
"""
        self.conf.update(dict(content = content, indent = '',  attributes_dict = attributes))
        self.body = body
        
class raised(indent_setter, abstract_object):
    """
    See http://materializecss.com/buttons.html
    user help : >> help (raised.init)
        Guide:
            button1 = raised(icon = icon('add_alarm'), name = "YHZ", href = 'https://www.baidu.com') 
    """
    @default_attr(attr = 'class', value = 'waves-effect waves-light btn')
    def init(self, **attributes):
        sugar = attrset_sugar(self.conf, attributes)
        sugar("name", "button")
        sugar("icon", None)
        self.body = \
"""
<a {{attributes_dict}}>{% if icon %}{{icon}}{% endif %}{{name}}</a>
"""
        self.conf.update(dict(indent = '',  attributes_dict = attributes))
        
        