from . import foreach, andThen, compose, fastmap
from .utils import dict_str

from jinja2 import Template
from copy import deepcopy

"""Some default configurations are defined here."""
default_conf=dict(Indent_unit = "    ") 

def gen_helper(render : dict):
    """
    Recursively render the objects.
    """
    if isinstance(render, str):
        return render
    else:
        return render -> foreach(_)( component_deal -> andThen(_)(dict_deal) ) ->render  where:
            
            get_type  = . obj  -> obj.__class__
            checktype = . type -> . obj -> get_type(obj) -> issubclass( _ , type)
        
            component_deal = as-with conf_key def conf_key where:
                
                condic render[conf_key]:
                    
                    (checktype(abstract_object))
                    case True               => 
                        render[conf_key] =  render[conf_key].gen()
                     
                    (get_type)
                    case dict               =>
                        render[conf_key] =  render[conf_key] -> gen_helper(_)
                
                    (get_type)
                    case Seq                =>
                        render[conf_key] = render[conf_key] -> fastmap(_)(gen_helper) -> tuple(_)
                     
                    otherwise               =>
                        pass
                
            dict_deal      = as-with conf_key def conf_key where:
                if render[conf_key] -> get_type(_) == dict:
                    render[conf_key] = dict_str(render[conf_key])
                
""" Meta """
                
class abstract_object:
    """
    Everything in Materialize-CSS has been abstracted to this Class.
    Everything in Materialize-CSS has 2 methods in common:
        1. setIndent :: int -> None
            If inherit the Class  "indent_setter"
            
                Recursively change the indentation of the object with the following rules:
                    <subobject's indentation>  = <indentation> + 1
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
        

    def setIndent(self, i:int):
        """
        Default to do nothing for some items without indentation. 
        Inherit the Class "indent_setter" to set Indent recursively.
        PS: Inherit the Class "indent_setter" before inheriting "abstract_object".
        """
        pass
    
    def gen(self):
        """
        Generate the html codes from the object.
        """
        render = deepcopy(self.conf)
        return eval("Template(self.body).render(**gen_helper(render) )")
    def common_init(self):
        """
        Do some common initial actions when initializing the Materialize-CSS object.
        """
        self.conf.update(default_conf)


""" Trait """

class indent_setter:
    """
    A trait of the objects in Materialize-CSS.
    To set the indentations of objects recursively.
    """
    def setIndent(self, i:int):
        self.conf["indent"] = i*default_conf["Indent_unit"] 
        self.conf -> foreach(_)(job) where:
            job = as-with conf_key def None where:
                if self.conf[conf_key] -> isinstance(_,  abstract_object):
                    _.setIndent(i+2)
                    
class Seq(list):
    """
    A trait of the objects in Materialize-CSS.
    This trait means that an object can have multiple items to be rendered, for instance:
        * form
        * table
        * row
    """
    def __init__(self, *args):
        return super(Seq, self).__init__(args)
                    
                    


