from struct4py import Struct

# Example usage
data = Struct(False)  # allow override: True by default
data.a = 10
print(data)  # {'a': 10}

data.a.b = 3  # will fail
