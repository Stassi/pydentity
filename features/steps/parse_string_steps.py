from behave import given, when, then
from behave.runner import Context
from src.parse_string import parse_string


@given("the unparsed input {value}")
def step_given_input(context: Context, value: str) -> None:
    """
    Store the given input value in the context.

    :param context: Behave's context object, which stores information and state for the duration of the test scenario.
    :param value: The input.
    """
    context.input_value = value


@when("the input is parsed")
def step_when_input_parsed(context: Context) -> None:
    """
    Parse the input and store the result in the context.

    :param context: Behave's context object, which stores information and state for the duration of the test scenario.
    """
    context.parsed = parse_string(context.input_value)


@then("the parsed input should be {value} of type {expected_type}")
def step_then_verify_parsed_input_and_type(context: Context, value: str, expected_type: str) -> None:
    """
    Verify the parsed input matches the expected value and type.

    :param context: Behave's context object, which stores information and state for the duration of the test scenario.
    :param value: The expected string.
    :param expected_type: The expected type of the parsed input.
    """
    expected = parse_string(value)
    assert context.parsed == expected, (
        f"Expected {context.parsed} to be {expected}"
    )

    assert type(context.parsed).__name__ == expected_type, (
        f"Expected {context.parsed} to be of type {expected_type}"
    )
