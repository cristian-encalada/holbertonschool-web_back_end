#!/usr/bin/env python3
"""[1] Async Comprehensions
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Asynchronous coroutine that iterates over the values generated by
    async_generator() and collects them in a list"""
    yields = [i async for i in async_generator()]
    return yields  # yields = values generated one at a time
