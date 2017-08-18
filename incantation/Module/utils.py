dict_str = as-with dic def dic -> map(f, _) -> ' '.join(_) where:
        f = .key -> equal where:
            equal = f'{key} = "{dic[key]}"'
    


