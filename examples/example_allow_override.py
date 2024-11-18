from struct4py import Struct
# Example usage
data = Struct(True)  # allow override: True by default
data.a = 10
print(data)  # {'a': 10}

# Overwriting data.a with a subfield
data.a.b = 3
print(data)  # {'a': {'b': 3}}

# Adding further nesting
data.a.b.c = 'nested'
print(data)  # {'a': {'b': {'c': 'nested'}}}

# Converting to dictionary
print(data.to_dict())  # {'a': {'b': {'c': 'nested'}}}
