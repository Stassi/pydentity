Feature: Parse string
  The parse string function parses a string and returns the appropriate type.

  Scenario Outline: Parsing various inputs
    Given the input <input>
    Then the parsed input is the result
    And the result should be <input>
    And the result type should be <type>

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
