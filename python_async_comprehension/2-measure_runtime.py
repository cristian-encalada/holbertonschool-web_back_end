#!/usr/bin/env python3
"""[2] Run time for four parallel comprehensions
"""
import asyncio
import time
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Measures the runtime of async_comprehension()
    """
    start_time = time.time()
    # waits for all the async operations to complete
    await asyncio.gather(async_comprehension())
    end_time = time.time()
    return end_time - start_time
