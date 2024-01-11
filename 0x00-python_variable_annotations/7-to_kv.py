#!/usr/bin/env python3
"""
    Module of to_kv function
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float], ) -> Tuple[str, float]:
    """
        Function that returns a Tuple

        Return:
            a Tuple of the given paramters
    """
    return k, v ** 2.0
