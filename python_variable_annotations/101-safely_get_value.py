#!/usr/bin/env python3
"""[11] More involved type annotations
"""
from typing import Mapping, Union, Any, TypeVar
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None]) -> Union[Any, T]:  # noqa: E501
    """Type-annotated function using TypeVar"""
    if key in dct:
        return dct[key]
    else:
        return default
