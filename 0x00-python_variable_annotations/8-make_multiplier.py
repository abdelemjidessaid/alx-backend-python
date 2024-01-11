#!/usr/bin/env python3
"""
    Module of make_multiplier function
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        Function that returns a Callable

        Return:
            a Callable
    """
    def multiply(x: float) -> float:
        """
            Function that returns the float x multiplied with float multiplier

            Return:
                a Float number
        """
        return x * multiplier

    return multiply
