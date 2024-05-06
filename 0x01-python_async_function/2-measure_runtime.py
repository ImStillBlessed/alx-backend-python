#!/usr/bin/env python3
'''
module has 1 func.
'''
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """.retuns tge total time for tge whole async"""
    start = time.time()
    await wait_n(n, max_delay)
    total_delay = time.time() - start
    return total_delay / n
