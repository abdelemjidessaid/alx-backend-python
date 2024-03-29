#!/usr/bin/env python3
"""
    Module of sum_list function
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
        Function that returns the sum of a list elements

        Return:
            a Float number which is the summation of input_list elements
    """

    sum: float = 0
    for n in input_list:
        sum = sum + n
    return sum
