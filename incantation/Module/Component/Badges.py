#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 14:53:43 2017

@author: misakawa
"""

from ..abst import abstract_object,indent_setter, Seq, default_attr, attrset_sugar
class collections(indent_setter, abstract_object):
    """
    See http://materializecss.com/badges.html
    user help : >> help (collections.init)
        Guide:
            >> cs = collections([dict(new = False,href = '#!', num = 1, name = 'Alan'),
                                 dict(new = True, href = '#!', num = 4, name = 'Alan'),
                                 dict(href = '#!', name = 'Alan'),
                                 dict(new = False,href = '#!', num = 14,name = 'Alan')
                                ],
                                )
            >> cs
              <div class="collection">
                  <a href="#!" class="collection-item"><span class="badge">1</span>Alan</a>
                  <a href="#!" class="collection-item"><span class="new badge">4</span>Alan</a>
                  <a href="#!" class="collection-item">Alan</a>
                  <a href="#!" class="collection-item"><span class="badge">14</span>Alan</a>
              </div>
    """
    @default_attr(attr = 'class', value = "collection")
    def init(self, content : (list,[dict]), **attributes):
        body   = \
"""
{{indent}}<div {{attributes_dict}}>
{{indent+Indent_unit}}{% for item in content%}
{{indent+Indent_unit*2}}<a href="{{item.href}}" class="collection-item">{%if 'new' in item %}<span class="{%if item.new %}new {% endif %}badge">{{item.num}}</span>{% endif %} {{item.name}}</a>
{{indent+Indent_unit}}{% endfor %}
{{indent}}</div>
"""      
        self.conf.update(dict(content = content, indent = '',  attributes_dict = attributes))
        self.body = body
        
    
class dropdown(indent_setter, abstract_object):
    """
    See http://materializecss.com/badges.html
    user help : >> help (dropdown.init)
         Guide:
             
    """
    def init(self, content:(list,[dict]), **attributes:dict(material_icons = 'arrow_drop_down')):
        body = \
"""
{{indent}}<ul id="{{id}}" class="dropdown-content">
{{indent+Indent_unit}}{% for item in content%}
{{indent+Indent_unit*2}}<li><a href="{{item.href}}" class="collection-item">{%if 'new' in item %}<span class="{%if item.new %}new {% endif %}badge">{{item.num}}</span>{% endif %} {{item.name}}</a></li>
{{indent+Indent_unit}}{% endfor %}
{{indent}}</ul>
{{indent}}<a {{attributes_dict}} data-activates="{{id}}">{{name}}<i class="material-icons right">{{material_icons}}</i></a>
           
"""
        sugar = attrset_sugar(self.conf, attributes)
        sugar('name', 'Dropdown[name = ???]')
        sugar('id', 'ID[unknown]')
        sugar('material_icons', 'arrow_drop_down')
        
        @default_attr(attr = 'class', value = 'btn dropdown-button')
        @default_attr(attr = 'href' , value = '#!')
        def  _init_(content:(list,[dict]), **attributes):
            self.conf.update(dict(content = content, indent = '',  attributes_dict = attributes))
            self.body = body
        _init_(content, **attributes)
        
    
    
        