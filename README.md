# pydentity

[![Continuous Integration](https://github.com/Stassi/pydentity/actions/workflows/ci.yml/badge.svg)](https://github.com/Stassi/pydentity/actions/workflows/ci.yml)
[![Security](https://github.com/Stassi/pydentity/actions/workflows/security.yml/badge.svg)](https://github.com/Stassi/pydentity/actions/workflows/security.yml)

## API

`T` is a [generic type](https://docs.python.org/3/library/typing.html#typing.Generic).

| Method            | Signature     | Description                                                  |
|-------------------|---------------|--------------------------------------------------------------|
| `identity`        | `T → T`       | Returns its value unchanged.                                 |
| `create_identity` | `T → (T → T)` | Returns a type-specific identity function of the given type. |

## Usage

### Identity function

The **identity function** (`T → T`) is a foundational type-versatile utility function capable of returning its input
value unchanged.

```python
from src.identity import identity

identity('hello')
# returns "hello"

identity(1)
# returns 1

```

### Type-specific identity function

Use `create_identity` to **create a type-specific identity function** (`T → (T → T)`) by calling `create_identity(type)`
where a [type](https://docs.python.org/3.11/library/stdtypes.html) is its only argument.

#### Example

To **create an example identity function** that only returns `str`s (strings):

```python
from src.identity import create_identity

string_identity = create_identity(str)

string_identity('hello')
# returns "hello"

string_identity(1)
# raises TypeError: Expected value of type "str", got "int"
```

#### Supported argument types

**Supported argument types** include and are not limited to:

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
