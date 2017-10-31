#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 22:42:38 2017

@author: misakawa
"""


from ..abst import abstract_object,indent_setter, default_attr, attrset_sugar, Seq

class navbar(indent_setter, abstract_object):
    """
    See http://materializecss.com/navbar.html
    user help : >> help (navbar.init)
        Guide:
            navbar(
                   [dict(href = 'https://baidu.com',  name = 'link1'),
                    dict(href = 'https://google.com', name = 'link2')
                   ],
                   href = 'https://github.com/thautwarm', 
                   name = 'Logo'
                   )
    """
    def init(self, content:(Seq,'or',list,'or', tuple), **attributes):
        sugar = attrset_sugar(self.conf, attributes)
        sugar('href', '!#')
        sugar('loc', 'left')
        sugar('name', 'Logo')
        sugar('ul_id', 'nav-mobile')
        self.conf['loc'] = ('left', 'right') if self.conf['loc']  == 'left' else ('right', 'left')
        
        condef content:
            {.obj, typefamily -> type(obj) in typefamily}
            case {list,tuple} =>
                body = \
"""
{{indent}}<nav>
{{indent+Indent_unit}}<div {{attributes_dict}}>
{{indent+Indent_unit}}<a href="{{href}}" class="brand-logo {{loc[0]}}">{{name}}</a>
{{indent+Indent_unit}}<ul id="{{ul_id}}" class="{{loc[1]}} hide-on-med-and-down">
{{indent+Indent_unit}}{% for item in content %}
{{indent+Indent_unit*2}}<li><a href="{{item.href}}">{{item.name}}</a></li>
{{indent+Indent_unit}}{% endfor %}
{{indent+Indent_unit}}</ul>
{{indent+Indent_unit}}</div>
{{indent}}</nav>
"""
            (.x->isinstance(x, abstract_object))
            case True =>
                body = \
"""
{{indent}}<nav>
{{indent+Indent_unit}}<div {{attributes_dict}}>
{{indent+Indent_unit}}<a href="{{href}}" class="brand-logo {{loc[0]}}">{{name}}</a>
{{indent+Indent_unit}}<ul id="{{ul_id}}" class="{{loc[1]}} hide-on-med-and-down">
{{indent+Indent_unit*2}}{{content}}
{{indent+Indent_unit}}</ul>
{{indent+Indent_unit}}</div>
{{indent}}</nav>
"""
        @default_attr(attr = 'class', value = 'nav-wrapper')
        def _init_(content, **attributes):
            self.conf.update(dict(content = content, indent = " ", attributes_dict = attributes))
            self.body = body
        _init_(content, **attributes)
        
        
