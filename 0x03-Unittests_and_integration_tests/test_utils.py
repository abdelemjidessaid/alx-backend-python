#!/usr/bin/env python3
"""
    Module contains test function that tests utils.py
"""
import unittest
access_nested_map = __import__('utils').access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
        Class TestAccessNestedMap inherits from unittest
        to test the functions of utils.py file
    """

    def test_access_nested_map(self):
        """
            Method that test the nested_map function
        """
        self.assertEqual(access_nested_map({"a": 1}, path=("a",)), 1)
        self.assertEqual(access_nested_map({"a": {"b": 2}}, path=("a",)), {"b": 2})
        self.assertEqual(access_nested_map({"a": {"b": 2}}, path=("a", "b")), 2)
