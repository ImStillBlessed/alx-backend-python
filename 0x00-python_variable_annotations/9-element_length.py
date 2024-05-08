#!/usr/bin/env python3
"""module has one func"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing elements
    from the input list along with their lengths.

    Args:
        lst (Iterable[Sequence]): The input list containing sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where
        each tuple contains an element from the input list
        along with its length.
    """
    return [(i, len(i)) for i in lst]
