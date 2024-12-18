# PyDefault - Uniform Default Values for Python

PyDefault allows for uniform assignment/generation of default values for common types in Python. The API comes in two forms - a function and a map.

## Function API

```py
from pydefault import default

class Person: ...

mynum = default(int) # initializes to 0
empty_list = default(list) # initializes to []

obj = default(Person) # initializes to None
```

## Map API

```py
from pydefault import default

class Person: ...

mynum = default[int] # initializes to 0
empty_list = default[list] # initializes to []

obj = default[Person] # initializes to None
```

## Default Values

The following types resolve to the following default values:
- `int` -> `0`
- `bool` -> `0` (`False`)
- `complex` -> `complex()`
- `str` -> `""`
- `float` -> `0.0`
- `list` -> `[]`
- `set` -> `set()`
- `dict` -> `{}`
- anything else -> `None`