#!/usr/bin/env python3
'''
This module contains 1 function.
'''
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Returns the average time per call for the wait_n coroutine.

    Args:
        n (int): Number of times to spawn wait_n.
        max_delay (int): Maximum delay in seconds for each wait_n call.
    Returns:
        float: The average time per call.
    """
    start = time.time()
    await wait_n(n, max_delay)
    total_delay = time.time() - start
    return total_delay / n
