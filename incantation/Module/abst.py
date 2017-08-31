from . import foreach, andThen, compose, fastmap
from .utils import dict_str, default_attr,dict_init_key, JS_template, attrset_sugar
from collections import defaultdict
from jinja2 import Template
from copy import deepcopy

"""Some default configurations are defined here."""
default_conf=dict(Indent_unit = "    ") 
get_type  = . obj  ->  obj.__class__
checktype = . type -> .obj -> get_type(obj) -> issubclass(_, type)
def gen_helper(render) -> ('dict -> dict', 'otherwise -> str'):
    """
    Recursively render the objects.
    """
    condef render:
        
        (get_type)
        case dict               =>
            render ->> foreach( key_func ) where:
                key_func = as-with key def None where:
                    render[key] = gen_helper(render[key]) -> _ if key != 'attributes_dict' else dict_str(_)
                    
        (checktype(abstract_object))
        case True               => 
            render = render.gen()
      
                    
        (get_type)
        case Seq                =>
            render = render ->> fastmap(gen_helper) => tuple => '\n'.join
            
        otherwise               =>
                        pass
    return render
                
""" Meta """
                
class abstract_object:
    """
    Everything in Materialize-CSS has been abstracted to this Class.
    Everything in Materialize-CSS has 2 methods in common:
        1. setIndent :: int -> None
            If inherit the Class  "indent_setter"
            
                Recursively change the indentation of the object with the following rules:
                    <subobject's indentation>  = (<indentation> + 2) * Indent_unit
                    "Indent_unit" is defined in "incantation.Module.abst.default_conf"
                    
            Else 
                Do Nothing
                
        2. gen :: () -> str
            Generate the html codes from the object.
    """
    def __init__(self,*args,**kwargs):
        self.conf = dict()
        self.body = ""
        eval("self.init(*args,**kwargs)")
        self.common_init()
        self.JS = ""
        

    def setIndent(self, i:int):
        """
        Default to do nothing for some items without indentation. 
        Inherit the Class "indent_setter" to set Indent recursively.
        PS: Inherit the Class "indent_setter" before inheriting "abstract_object".
        """
        return self
    
    def gen(self):
        """
        Generate the html codes from the object.
        """
        render   = deepcopy(self.conf)
        rendered =  eval("Template(self.body).render(**gen_helper(render) )")
        if self.JS:
            rendered = rendered + JS_template.format(JS = (self.conf['indent']+default_conf['Indent_unit']).join(self.JS.splitlines()), 
                                                     indent =self.conf['indent'], 
                                                     Indent_unit =default_conf['Indent_unit'])
        return rendered
        
    def common_init(self):
        """
        Do some common initial actions when initializing the Materialize-CSS object.
        """
        self.conf.update(default_conf)
    
    def cons_class(self, string:str):
        dict_init_key(self.conf['attributes_dict'])('class', str)
        self.conf['attributes_dict']['class'] = f"{string} {self.conf['attributes_dict']['class']}"
        return self
    
    def append_class(self, string:str):
        dict_init_key(self.conf['attributes_dict'])('class', str)
        self.conf['attributes_dict']['class'] += f" {string}"
        return self
    
    def cons_attr(self, attr:str):
        dict_init_key(self.conf['attributes_dict'])(attr, str)
        def _f(string:str):
            self.conf['attributes_dict'][attr] = f"{string} {self.conf['attributes_dict'][attr]}"
            return self
        return _f
    
    def append_attr(self, attr:str):
        dict_init_key(self.conf['attributes_dict'])(attr, str)
        def _f(string:str):
            self.conf['attributes_dict'][attr] += f" {string}"
            return self
        return _f
    
        


""" Trait """

class indent_setter:
    """
    A trait of the objects in Materialize-CSS.
    To set the indentations of objects recursively.
    """
    def setIndent(self, i:int):
        self.conf["indent"] = i*default_conf["Indent_unit"] 
        self.conf ->> foreach(job) where:
            job = as-with conf_key def None where:
                if   self.conf[conf_key] -> isinstance(_,  indent_setter):
                     _.setIndent(i+2)
                elif self.conf[conf_key] -> isinstance(_,  Seq):
                    foreach(for_each_item)(_) where:
                        for_each_item = . each_item ->  None where:
                            if isinstance(each_item, indent_setter):
                                each_item.setIndent(i+2)
        return self
                    
class Seq(list):
    """
    A kind of container of the objects in Materialize-CSS.
    This trait means that an object can have multiple items to be rendered, for instance:
        * form
        * table
        * row
    For example:
         cols = Seq(
                col(content1, dict(m=6,s=12,l=12)), 
                col(content2, dict(m=6,s=12,l=12)),
                col(content3, dict(m=6,s=12,l=12))
            )
         Row = row(cols)
    """
    def __init__(self, *args):
        return super(Seq, self).__init__(args)
    

                    
                    


