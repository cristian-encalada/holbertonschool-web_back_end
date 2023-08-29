#!/usr/bin/env python3
"""[1] Execute multiple coroutines at the same time with async
"""
import asyncio
from typing import List
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Asynchronous coroutine that spawn wait_random n times with
    the specified max_delay and returns the list of all the delays
    """
    delays = []
    for iteration in range(n):
        delays.append(await wait_random(max_delay))
    return sorted(delays)
