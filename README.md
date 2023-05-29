# pydentity

[![Continuous Integration](https://github.com/Stassi/pydentity/actions/workflows/ci.yml/badge.svg)](https://github.com/Stassi/pydentity/actions/workflows/ci.yml)
[![Security](https://github.com/Stassi/pydentity/actions/workflows/security.yml/badge.svg)](https://github.com/Stassi/pydentity/actions/workflows/security.yml)

**`pydentity`** is an implementation of [identity functions](https://en.wikipedia.org/wiki/Identity_function) designed
for various practical applications in Python development
and [functional programming](https://en.wikipedia.org/wiki/Functional_programming).

## API

### `identity` (`T → T`)

The **identity function** is a generic function that takes a value of any type and returns it unchanged.

#### Example usage

```python
from src.identity import identity

identity('hello')  # returns "hello"
identity(1)  # returns 1
```

### `create_identity` (`T → (T → T)`)

This function takes a type as an argument and returns a **type-specific identity function**. If the type-specific
function is called with a value that doesn't match the specified type, it will raise a `TypeError`.

#### Example usage

```python
from src.identity import create_identity

string_identity = create_identity(str)

string_identity('hello')  # returns "hello"
string_identity(1)  # raises TypeError: Expected value of type "str", got "int"
```

#### Types supported

A wide range of **[built-in types](https://docs.python.org/3/library/stdtypes.html) are supported**:

* `bool`
* `bytes`
* `dict`
* `ellipsis`
* `float`
* `int`
* `list`
* `set`
* `str`
* `tuple`
* `NoneType`
