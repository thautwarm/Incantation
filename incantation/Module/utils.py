dict_str = as-with dic def dic -> map(f, _) -> ' '.join(_) where:
        f = .key -> equal where:
            equal = f'{key} = "{dic[key]}"'
    
default_attr = . attr, value -> .func -> _f where:
    def _f(*args, **attributes):
        if attr not in attributes:
            attributes[attr] = value
        elif value not in attributes[attr]:
            attributes[attr] = f"{value} " + attributes[attr] 
        return func(*args, **attributes)


