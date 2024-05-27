#!/usr/bin/env python3
"""Test module for GithubOrgClient class"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for the GithubOrgClient class"""

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, expected, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value.
        """
        mock_get_json.return_value = expected
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected)
        mock_get_json.assert_called_once_with(client.ORG_URL
                                              .format(org=org_name))

    def test_public_repos_url(self):
        """Test the _public_repos_url property"""
        with patch.object(GithubOrgClient, 'org',
                          new_callable=PropertyMock) as mock_org:
            url = "https://api.github.com/orgs/google/repos"
            mock_org.return_value = {"repos_url": url}
            client = GithubOrgClient("google")
            self.assertEqual(client._public_repos_url, url)
            mock_org.assert_called_once()

    @patch('client.get_json')
    @patch.object(GithubOrgClient, '_public_repos_url',
                  new_callable=PropertyMock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """Test the public_repos method"""
        public_url = "https://api.github.com/orgs/google/repos"
        mock_public_repos_url.return_value = public_url
        payload = [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}},
            {"name": "repo3", "license": {"key": "mit"}}
        ]
        mock_get_json.return_value = payload
        client = GithubOrgClient("google")
        repos = client.public_repos(license="mit")

        excepted_repos = ["repo1", "repo3"]
        self.assertEqual(repos, excepted_repos)

        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with(public_url)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test the has_license method"""
        client = GithubOrgClient("google")
        result = client.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class(('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
                     [(org_payload, repos_payload, expected_repos, apache2_repos)])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test cases for the GithubOrgClient class"""

    @classmethod
    def setUpClass(cls):
        """Set up the test class"""
        cls.get_patcher = patch('client.requests.get')
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Tear down the test class"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test the public_repos method"""
        self.mock_get.return_value.json.return_value = self.org_payload
        self.mock_get.return_value.json.side_effect = [self.repos_payload]
        client = GithubOrgClient("google")
        repos = client.public_repos(license="apache-2.0")

        self.assertEqual(repos, self.apache2_repos)


if __name__ == '__main__':
    unittest.main()
