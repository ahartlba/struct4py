# struct4py

![Unittest](https://github.com/ahartlba/struct4py/actions/workflows/testing.yml/badge.svg?branch=main)
![Static Badge](https://img.shields.io/badge/https%3A%2F%2Fimg.shields.io%2Fbadge%2Fcode%2520style-black-black?label=codestyle)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/decorator-validation)
[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)

Matlab like structure for python

An example on how to use it in your workflow.
Functions like Matlab structs where you can directly assign multiple levels of data.

By default it allows overriding

```py
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
```

but this can easily be prevented with a single flag

```py
data = Struct(False)  # allow override: True by default
data.a = 10
print(data)  # {'a': 10}
```
