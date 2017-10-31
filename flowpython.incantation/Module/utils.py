dict_str = as-with dic def dic -> map(f, _) ->> ' '.join where:
        f = .key -> equal where:
            equal = f'{key} = "{dic[key]}"'
    
default_attr = . attr, value -> .func -> _f where:
    def _f(*args, **attributes):
        if attr not in attributes:
            attributes[attr] = value
        elif value not in attributes[attr]:
            attributes[attr] = f"{value} " + attributes[attr] 
        return func(*args, **attributes)

attrset_sugar = as-with conf, attributes def as attr, value def None where:
    if attr in attributes: 
        conf[attr] = attributes[attr]
        del attributes[attr]
    else:
        conf[attr] = value
    


dict_init_key = . dic -> . attr, type -> None where:
        if attr not in dic:
            dic[attr] = type()
            
            
JS_template =\
"""
{indent}<script>
{indent}{Indent_unit}{JS}
{indent}</scirpt>
"""

class ANY:
    def __eq__(self,v):
        return True
Any = ANY()

class Rule:
    def __init__(self, f):
        self.f = f
    def __eq__(self, v):
        if self.f(v):
            return True
        else:
            return False
        
        
        
        

    