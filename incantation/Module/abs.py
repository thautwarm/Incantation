from jinja2 import Template
from . import foreach
from .utils import dict_str

def dict_deal(self):
    for conf_key in self.conf:
        if conf_key.endswith("_dict"):
            self.conf[f"{conf_key}_str"] = dict_str( self.conf.pop(conf_key) )
    return self.conf
class indent_setter:
    def setIndent(self, i):
        for conf_key in self.conf:
            pass
    
class abstract_component:
    
    def setIndent(self, i):pass
    
    def gen(self):
        return eval("Template(self.body).render(**dict_deal(self) )")



