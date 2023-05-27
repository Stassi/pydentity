Feature: Type-specific identity function
  The type-specific identity function is created by the higher-order function create_identity, which returns a specialized identity function for the given type.

  Scenario Outline: Apply type-specific identity function to various types of input
    Given the input <input>
    And the type-specific identity function for type <type>
    When the type-specific identity function is applied
    Then the result should be <input>

    Examples:
      | input            | type     |
      | False            | bool     |
      | True             | bool     |
      | b"hello"         | bytes    |
      | {"a": 1, "b": 2} | dict     |
      | ...              | ellipsis |
      | -1.23            | float    |
      | 1.23             | float    |
      | -1.2e3           | float    |
      | 1.2e-3           | float    |
      | -42              | int      |
      | 42               | int      |
      | [1, 2, 3]        | list     |
      | {1, 2, 3}        | set      |
      | set()            | set      |
      | "hello"          | str      |
      | (1, 2, 3)        | tuple    |
      | None             | NoneType |
