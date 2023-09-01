#!/usr/bin/env python3
"""[11] More involved type annotations
"""
from typing import Mapping, Union, Any, TypeVar
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: T = None) -> Union[Any, T]:
    """Type-annotated function using TypeVar"""
    if key in dct:
        return dct[key]
    else:
        return default
