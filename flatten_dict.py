from collections import defaultdict

def flatten_dict(d, parent_key='', sep='_'):
    items = defaultdict(list)
    
    def _flatten(inner_d, parent_key):
        if isinstance(inner_d, dict):
            for k, v in inner_d.items():
                new_key = f"{parent_key}{sep}{k}" if parent_key else k
                if isinstance(v, dict):
                    _flatten(v, new_key)
                elif isinstance(v, list) and all(isinstance(i, dict) for i in v):
                    for item in v:
                        _flatten(item, new_key)
                else:
                    items[new_key].append(v)
        elif isinstance(inner_d, list):
            for item in inner_d:
                _flatten(item, parent_key)
        else:
            items[parent_key].append(inner_d)
    
    _flatten(d, parent_key)
    
    # Convert defaultdict to a regular dictionary for the final result
    return {k: v if len(v) > 1 else v[0] for k, v in items.items()}

# Example usage:
nested_dict_with_list = {
    'a': 1,
    'b': {
        'c': 2,
        'd': {
            'e': 3,
            'f': 4
        },
        'g': [
            {'h': 5, 'i': 6},
            {'h': 7, 'i': 8}
        ]
    },
    'k': 9
}

flattened_dict = flatten_dict(nested_dict_with_list)
print(flattened_dict)
