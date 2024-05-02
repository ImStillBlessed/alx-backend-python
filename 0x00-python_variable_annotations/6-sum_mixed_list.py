#!/usr/bin/env python3
"""Module to calculate the sum of a mixed list
of integers and floats"""

from typing import List, Union

def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    Calculates the sum of a mixed list of integers and floats.
    Args:
        mxd_list (List[Union[int, float]]): The list containing
        integers and floats.
    Returns:
        float: The sum of the values in the mixed list.
    """
    return sum(mxd_list)
