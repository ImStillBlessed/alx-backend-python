#!/usr/bin/env python3
"""damn documentayion, im tired"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Converts a key-value pair into a tuple.

    Args:
        k (str): The key as a string.
        v (Union[int, float]): The value as an integer or float.

    Returns:
        Tuple[str, float]: A tuple containing the key and the value.
    """
    return (k, v)
