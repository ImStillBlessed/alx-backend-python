#!/usr/bin/env python3
"""This module has 1 function"""

import asyncio
from typing import AsyncGenerator
import random

async def async_generator() -> AsyncGenerator[float, None]:
    """"
    This mehod is a coroutine called async_generator that takes no arguments.
    The coroutine will loop 10 times,
    each time asynchronously wait 1 second,
    then yield a random number between 0 and 10. Use the random module.
    """
    # return [random.uniform(0, 10) async for _ in range(10)
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
