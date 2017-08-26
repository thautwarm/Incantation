#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 16:14:34 2017

@author: misakawa
"""
from ..abst import abstract_object,indent_setter, Seq
class table(indent_setter, abstract_object):
    """
    See http://materializecss.com/table.html
    user help : >> help (table.init)
    """
    
    def init(self, column_names : list, data : list,   **attributes):
        """
        Guide:
            >> 
        """
        body = \
"""
{{indent}}<table {{attributes_dict}}>
{{indent+Indent_unit}}<thead>
{{indent+Indent_unit*2}}<tr>
{{indent+Indent_unit*2}}{% for column_name in column_names%}
{{indent+Indent_unit*3}}<th>{{column_name}}</th>
{{indent+Indent_unit*2}}{% endfor %}
{{indent+Indent_unit*2}}</tr>
{{indent+Indent_unit}}</thead>
{{indent+Indent_unit}}<tbody>
{{indent+Indent_unit*2}}{% for item in data%}
{{indent+Indent_unit*2}}<tr>
{{indent+Indent_unit*3}}{% for cell in item%}
{{indent+Indent_unit*3}}<td>{{cell}}</td>
{{indent+Indent_unit*3}}{% endfor %}
{{indent+Indent_unit}}</tr>
{{indent+Indent_unit*2}}{% endfor %}
{{indent+Indent_unit}}</tbody>
{{indent}}</table>
"""
        self.conf.update(indent = " ", data = data, column_names = column_names, attributes_dict = attributes)
        self.body = body
    
        