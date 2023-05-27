from behave import then
from behave.runner import Context


@then("the parsed input is the result")
def step_then_parsed_input_is_result(context: Context) -> None:
    """
    Store the parsed input as the result.

    :param context: Behave's context object, which stores information and state for the duration of the test scenario.
    """
    context.result = context.value


@then("the result type should be {expected_type}")
def step_then_verify_result_type(context: Context, expected_type: str) -> None:
    """
    Verify the result is of the expected type.

    :param context: Behave's context object, which stores information and state for the duration of the test scenario.
    :param expected_type: The expected type of the result.
    """
    assert type(context.value).__name__ == expected_type, f"Expected {context.value} to be of type {expected_type}"
