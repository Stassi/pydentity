from typing import Type

from behave import given, when
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
    context.result = context.type_specific_identity_function(context.value)
