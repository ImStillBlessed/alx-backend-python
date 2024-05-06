#!/usr/bin/env python3
"""This module has 1 function"""

import asyncio
import random


async def wait_random(max_delay: int =10) -> float:
    """
    This method waits a random number of seconds
    and prints the number
    args: max_delay int default 10.
    returns: the random float number.
    """
    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
