#!/usr/bin/env python3
"""[8] Complex types - functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Type-annotated function to return a function that multiplies a float
    by the multiplier argument"""
    def mult_func(num: float) -> float:
        return multiplier * num
    return mult_func
