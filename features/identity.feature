Feature: Identity function
  The identity function returns its input unchanged.

  Scenario Outline: Apply identity function to various types of input
    Given the input <input>
    When the identity function is applied
    Then the result should be <input>

    Examples:
      | input   |
      | True    |
      | False   |
      | 42      |
      | -42     |
      | 1.23    |
      | -1.23   |
      | 1.2e-3  |
      | -1.2e3  |
      | "hello" |
      | None    |
