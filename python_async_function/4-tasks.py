#!/usr/bin/env python3
"""[4] Tasks
"""
import asyncio
from typing import List
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Generates n tasks that simulate asynchronous delays
    """
    tasks = []
    for _ in range(n):
        tasks.append(task_wait_random(max_delay))
    # Executes the tasks concurrently using 'asyncio.gather'
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
