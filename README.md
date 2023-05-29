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

## Applications

### Placeholder

The `identity` function can be used as a [no-operation](https://en.wikipedia.org/wiki/NOP_(code)) **placeholder** during
the development process, especially in the early stages when components are pending implementation.

### Default function

The `identity` function can be employed as a **default function**, a fallback option for when a function is not supplied
during development.

### Type safety

The `create_identity` function ensures **[type safety](https://en.wikipedia.org/wiki/Type_safety)** by generating
type-specific identity functions in scenarios where type consistency is required.

### Higher-order functions

Identity functions can be used as arguments for **[higher-order
functions](https://en.wikipedia.org/wiki/Higher-order_function)** (**HOF**s), which accept other functions as
parameters.

### Functional pipelines

Identity functions, which leave their input unaltered, can be utilized in **[functional
composition](https://en.wikipedia.org/wiki/Function_composition_(computer_science))** (data transformation
pipelines), where a certain transformation might conditionally need to be skipped.
