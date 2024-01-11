#!/usr/bin/env python3
"""
    Module of sum_mixed_list
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
        Function that does a summation of mxd_list elements

        Return:
            a Float number which is the result of the summation
    """
    sum: float = 0
    for n in mxd_lst:
        sum = sum + n

    return sum
