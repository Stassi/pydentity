from typing import Type

from behave import given, then, when
from behave.runner import Context

from src.identity import create_identity, T

type_mapping: dict[str, Type[T]] = {
    "bool": bool,
    "bytes": bytes,
    "dict": dict,
    "ellipsis": type(Ellipsis),
    "float": float,
    "int": int,
    "list": list,
    "set": set,
    "str": str,
    "tuple": tuple,
    "NoneType": type(None),
}


@given("the type-specific identity function for type {type_str}")
def step_given_type_specific_identity_function(context: Context, type_str: str) -> None:
    """
    Create and store a type-specific identity function for the given type in the context.

    :param context: Behave's context object, which stores information and state for the duration of the test scenario.
    :param type_str: The type for which the identity function should be created.
    """
    context.type_specific_identity_function = create_identity(type_mapping[type_str])


@when("the type-specific identity function is applied")
def step_when_type_specific_identity_function_applied(context: Context) -> None:
    """
    Apply the type-specific identity function to the input value and store the result in the context.

    :param context: Behave's context object, which stores information and state for the duration of the test scenario.
    """
    try:
        context.result = context.type_specific_identity_function(context.value)
    except Exception as e:
        context.exception = e


@then('a TypeError should be raised with the message "{msg}"')
def step_then_type_error(context: Context, msg: str) -> None:
    """
    Expect a TypeError exception.

    :param context: Behave's context object, which stores information and state for the duration of the test scenario.
    :param msg: The expected TypeError message.
    """
    assert 'exception' in context, "Expected an exception but none was raised"
    assert isinstance(context.exception, TypeError), f'Expected TypeError, got "{type(context.exception).__name__}"'
    assert str(context.exception) == msg, f'Expected error message "{msg}", got "{str(context.exception)}"'
