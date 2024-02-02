#!/usr/bin/env python3
"""
    Module that contains test on test_client Module
"""
import unittest
from unittest.mock import Mock, patch, PropertyMock
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
            Method that tests the GithubOrgClient.org() Method
        """
        get_patch.return_value = expected
        instance = GithubOrgClient(org)
        self.assertEqual(instance.org, expected)
        get_patch.assert_called_once_with(
            f'https://api.github.com/orgs/{org}'
        )

    def test_public_repos_url(self):
        """
            Method that tests the GithubOrgClient._public_repos_url Method
        """
        expected = "abdelemjidessaid"
        payload = {"repos_url": expected}
        mocked_method = 'client.GithubOrgClient.org'
        with patch(mocked_method, PropertyMock(return_value=payload)):
            client = GithubOrgClient('heroshima')
            self.assertEqual(client._public_repos_url, expected)
