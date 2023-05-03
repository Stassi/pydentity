from behave import when
from behave.runner import Context

from src.identity import identity


@when('the identity function is applied')
def step_when_identity_function_applied(context: Context) -> None:
    """
    Apply the identity function to the input and store the result in the context.

    :param context: Behave's context object, which stores information and state for the duration of the test scenario.
    """
    context.result = identity(context.value)
