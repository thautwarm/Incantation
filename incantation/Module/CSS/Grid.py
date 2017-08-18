from ..abst import abstract_object,indent_setter, Seq, default_attr
from ..utils import Any,Rule
from ..abst import Template
class container(indent_setter, abstract_object):
    """
    See http://materializecss.com/grid.html.
    user help : >> help (container.init)
    """
    
    @default_attr(attr = "class", value = "container")
    def init(self, content = "" , **attributes):
        body   = \
"""
{{indent}}<div {{attributes_dict}}>
{{indent}}<!-- Page Content goes here -->
{{indent+Indent_unit}}{{content}}
{{indent}}</div>
"""            
        self.conf.update(dict(content = content, indent = '',  attributes_dict = attributes))
        self.body = body

    def contains(self, content):
        self.conf["content"] = content
        
    
class row(indent_setter, abstract_object):
    """
    See http://materializecss.com/grid.html.
    user help : >> help (grid.init)
    """
    
    @default_attr(attr = "class", value = "row")
    def init(self, content : Seq , **attributes):
        body = \
"""
{{indent}}<div {{attributes_dict}}>
{{indent+Indent_unit}}{{content}}
{{indent}}</div>
"""
        self.conf.update(dict(content = content, indent = " ", attributes_dict = attributes))
        self.body = body

class col(indent_setter, abstract_object):
    """
    See http://materializecss.com/grid.html.
    user help : >> help (col.init)
                >> col("some text", grid(m = 6, s= 6, l = 12))
    """
    def init(self, content, grid : "<class 'grid'>" ,  **attributes):
        body =\
"""
{{indent}}<div {{attributes_dict}}>
{{indent+Indent_unit}}{{content}}
{{indent}}</div>
"""
        @default_attr(attr = "class", value = grid.gen())
        def _init_(content, **attributes):    
            self.conf.update(dict(content = content, indent = " ", attributes_dict = attributes))
            self.body = body
        _init_(content, **attributes)
    
class divider(indent_setter, abstract_object):
    """
    See http://materializecss.com/grid.html.
    """
    def init(self,*args, **kwargs):
        self.body =\
"""
{{indent}}<div class="divider"></div>
"""
        self.conf.update(dict(indent = " "))
        
class section(indent_setter, abstract_object) :
    """
    See http://materializecss.com/grid.html.
    """
    @default_attr(attr = "class", value = "section")
    def init(self,content, **attributes):
        body =\
"""
{{indent}}<div {{attributes_dict}}>
{{indent+Indent_unit}}{{content}}
{{indent}}</div>
"""
        self.conf.update(dict(content = content, indent = '',  attributes_dict = attributes))
        self.body = body
        

class grid(abstract_object, dict):
    """
    grid(m = 1, s = 2 ,l =3).push
    default:
        s:m:l = 12 : 6 : 4
    
    user help:
        >>> col("content here!", grid(m=5, s= 8, l=3).roffset(grid(s=3,m=1,l=1)) )
    """    
    def init(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)       
        self.update(dict(loffset = (), roffset=() ))

        
        s = None if 's' not in self else self['s']
        m = None if 'm' not in self else self['m']
        l = None if 'l' not in self else self['l']
        condic[] (s,m,l):
            
            case (None, None, None) =>
                raise ValueError("Number of input arguments is zero!!! ")
            
            case (Rule(.x->x.__class__ is int), None, None) =>
                self['m'] = self['s']//2
                self['l'] = self['s']//3
            
            case (None, Rule(.x->x.__class__ is int), None) =>
                self['s'] = self['m']*2
                self['l'] = self['s']//3
            
            case (None, None, Rule(.x->x.__class__ is int)) =>
                self['s'] = self['l']*3
                self['m'] = self['s']//2
                
            (.x -> map(type, x) -> tuple(_))
            case (int,int,int)                              =>
                pass
            
            otherwise                                       =>
                raise ValueError("Do not support initializing the grid with these arguments!!!")
            
    
    def loffset(self, tup):
        condic tup:
            (type)
            case int =>
                self['loffset'] = dict(s = tup, m = tup//2, l = tup//3)
                
            (.x -> map(type, x.values()) -> tuple(_))
            case (int,int,int) =>
                self['loffset'] = tup
        
            otherwise          =>
                raise ValueError("Do not support setting left-offset with these arguments!!!")
        return self
    def push(self, tup): return self.loffset(tup)
    
                
    def roffset(self, tup):
        condic tup:
            (type)
            case int =>
                self['roffset'] = dict(s = tup, m = tup//2, l = tup//3)
                
            (.x -> map(type, x.values()) -> tuple(_))
            case (int,int,int) =>
                self['roffset'] = tup
        
            otherwise          =>
                raise ValueError("Do not support setting right-offset with these arguments!!!")
        return self
    def pull(self, tup): return self.roffset(tup)
    
    def gen(self):
        ret = Template("col s{{s}} m{{m}} l{{l}}").render(**self)
        if self['loffset']:
            ret += Template(" push-s{{s}} m{{m}} l{{l}}").render(**self['loffset'])
        if self['roffset']:
            ret += Template(" pull-s{{s}} m{{m}} l{{l}}").render(**self['roffset'])
        return ret
        
            

        
                
            
            
        

