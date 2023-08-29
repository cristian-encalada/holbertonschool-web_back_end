#!/usr/bin/env python3
"""[0] Async generator
"""
import asyncio
import random


async def async_generator():
    """Asynchronous coroutine that generates random float numbers"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
