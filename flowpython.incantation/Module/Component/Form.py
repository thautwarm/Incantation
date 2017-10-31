#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 21:29:47 2017

@author: misakawa
"""

from ..abst import abstract_object,indent_setter, attrset_sugar, Seq
from ..CSS.Grid import col

class input_field(col): 
    """
    See http://materializecss.com/forms.html
    user help : >> help (input_field.init)
        Guide:
            input_field(field_name = 'Username', type = 'text', icon = icon('mode_edit'), id = 'for-username')
    
        Take care for `submit`:
            submit = \
            input_field(field_name = "TiJiao/Submit",
                        type = 'submit',
                        icon = icon('publish'),
                        )
    """
    def init(self, grid : "CSS.Grid.grid" ,  **attributes):
        sugar = attrset_sugar(self.conf, attributes)
        sugar('icon', None)
        sugar('id', 'Some Id')
        sugar('type', 'text')
        sugar('field_name', 'Some Field')
        if self.conf['type'].lower() == 'submit':
            if 'class' not in attributes:
                attributes['class'] =  "waves-effect waves-light btn"
            else:
                attributes['class'] += "waves-effect waves-light btn"
            body =\
"""
{{indent}}<input {{attributes_dict}} id="{{id}}" name = "{{id}}" type = "{{type}}">
"""
        else:
            sugar('class', 'validate')
            body =\
"""
{{indent}}<div {{attributes_dict}}>
{{indent+Indent_unit}}<input id="{{id}}" name = "{{id}}" class="{{class}}" type = "{{type}}">
{{indent+Indent_unit}}<label for="{{id}}">{{field_name}}</label>
{{indent}}</div>
""" 
        self.conf.update(dict(indent = " ", attributes_dict = attributes))
        self.append_class(grid.gen())
        self.body = body
        self.cons_class("input-field")
        
        
class form(indent_setter, abstract_object):
    """
    See http://materializecss.com/forms.html
    user help : >> help (form.init)
        Guide:
            a_form = form(
                        Seq(
                        input_field(grid(s=12), field_name = 'Username', type = 'text',     icon = icon('mode_edit'), id = 'for-username'),
                        input_field(grid(s=12), field_name = 'Password', type = 'password', icon = icon('brightness_auto'),   id = 'for-password'),
                        input_field(grid(s=12), field_name = 'School',   type = 'text',     icon = icon('brightness_3'),   id = 'for-school'),
                        input_field(grid(s=12), field_name = 'submit',   type = 'submit',   icon = icon('publish'),   id = 'for-submit')->> right_align,
                        ),
                        action = 'script',
                        method = 'POST')
    """
    
    def init(self, content :(Seq,[input_field]), **attributes):
        body = \
"""
{{indent}}<form {{attributes_dict}}>
{{indent+Indent_unit}}{{content}}
{{indent}}</form>
"""
        self.conf.update(dict(content = content, indent = " ", attributes_dict = attributes))
        self.body = body



        