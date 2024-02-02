#!/usr/bin/env python3
"""
    Module that contains test on test_client Module
"""
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
import client
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
        TestGithubOrgClient class that inherits from unittest.TestCase
    """

    @parameterized.expand([
        ("google", {"google": True}),
        ("abc", {"abc": True})
    ])
    @patch('client.get_json')
    def test_org(self, org, expected, get_patch):
        """
            Method that tests the test_client.org() Method
        """
        get_patch.return_value = expected
        instance = GithubOrgClient(org)
        self.assertEqual(instance.org, expected)
        get_patch.assert_called_once_with(
            f'https://api.github.com/orgs/{org}'
        )
