#!/usr/bin/env python3
"""
    Module contains test function that tests utils.py
"""
import unittest
from parameterized import parameterized
access_nested_map = __import__('utils').access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
        Class TestAccessNestedMap inherits from unittest
        to test the functions of utils.py file
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
            Method that test the nested_map function
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)
