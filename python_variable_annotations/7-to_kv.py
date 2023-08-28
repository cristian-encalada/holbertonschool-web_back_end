#!/usr/bin/env python3
"""[7] Complex types - string and int/float to tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[Union[str, float]]:
    """Type-annotated function to return a string and int/float tuple"""
    return k, v*v
