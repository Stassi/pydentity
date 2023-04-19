Feature: Parse string
  The parse string function parses a string and returns the appropriate type.

  Scenario Outline: Parsing various inputs
    Given the unparsed input <input>
    When the input is parsed
    Then the parsed input should be <input> of type <type>

    Examples:
      | input   | type     |
      | True    | bool     |
      | False   | bool     |
      | 42      | int      |
      | -42     | int      |
      | 1.23    | float    |
      | -1.23   | float    |
      | 1.2e-3  | float    |
      | -1.2e3  | float    |
      | "hello" | str      |
      | None    | NoneType |
