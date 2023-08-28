#!/usr/bin/env python3
"""[5] Complex types - list of floats
"""
from typing import List  # fix for 'type' object is not subscriptable


def sum_list(input_list: List[float]) -> float:
    """Type-annotated function to sum a list of float numbers"""
    return sum(input_list)
