from behave import given, when, then
from behave.runner import Context

from src.identity import identity
from src.parse_string import parse_string


@given('the input {value}')
def step_given_input(context: Context, value: str) -> None:
    """
    Parse and store the input in the context.

    :param context: Behave's context object, which stores information and state for the duration of the test scenario.
    :param value: The input value.
    """
    context.value = parse_string(value)


@when('the identity function is applied')
def step_when_identity_function_applied(context: Context) -> None:
    """
    Apply the identity function to the input and store the result in the context.

    :param context: Behave's context object, which stores information and state for the duration of the test scenario.
    """
    context.result = identity(context.value)


@then('the result should be {value}')
def step_then_verify_result(context: Context, value: str) -> None:
    """
    Verify the result from applying the identity function matches the expected value.

    :param context: Behave's context object, which stores information and state for the duration of the test scenario.
    :param value: The expected value.
    """
    parsed_value = parse_string(value)
    assert context.result == parsed_value, f"Expected {parsed_value}, but got {context.result}"
