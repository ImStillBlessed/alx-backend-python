#!/usr/bin/env python3
"""this module contains 1 func"""
from typing import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns wait_random n times
    with the specified max_delay.
    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay in seconds for each wait_random call.
    Returns:
        List[float]: List of all the delays in ascending order.
    """
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)
