#!/usr/bin/env python3
"""module has one func"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): The multiplier to use for multiplication.

    Returns:
        Callable[[float], float]: A function that takes a float
        as input and returns the multiplied result.
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier
    return multiplier_function
