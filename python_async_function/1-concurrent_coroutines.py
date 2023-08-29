#!/usr/bin/env python3
"""[1] Execute multiple coroutines at the same time with async
"""
import asyncio
from typing import List
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Generates n coroutines that simulate asynchronous delays
    """
    delays = []
    for iteration in range(n):
        # Awaits each coroutine sequentially using 'await'
        delays.append(await wait_random(max_delay))
    return sorted(delays)
