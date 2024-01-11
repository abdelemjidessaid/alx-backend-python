#!/usr/bin/env python3
"""
    Module of element_length function
"""

from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
        Function that returns a list of tuples that
        contains a string and its length

        Return:
            List of Tuples of sequence, int
    """

    return [(i, len(i)) for i in lst]
