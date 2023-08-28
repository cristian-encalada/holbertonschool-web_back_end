#!/usr/bin/env python3
"""[8] Iterable object
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Type-annotated function for an Iterable object"""
    return [(i, len(i)) for i in lst]
