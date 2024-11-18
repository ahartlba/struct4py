from struct4py import Struct

# Example usage
data = Struct()

# Assigning primitive value
data.a = 10
print(data)  # Struct({'a': 10})
print(data.a)  # 10

data.b.c = 20
print(data.b.c)  # 20
print(data)  # Struct({'a': 10, 'b': Struct({'c': 20})})
