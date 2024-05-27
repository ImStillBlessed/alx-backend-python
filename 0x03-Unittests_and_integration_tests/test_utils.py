#!/usr/bin/env python3
"""
Test module for unittest tasks.

This module contains unit tests for functions defined in the utils module.
It includes tests for the following functions:
- access_nested_map
- get_json
- memoize
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
import utils


class TestAccessNestedMap(unittest.TestCase):
    """
    Test cases for the access_nested_map function.
    """

    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ('a',), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test that access_nested_map returns the expected
        result for valid paths.
        """
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ('a',)),
        ({'a': 1}, ('a', 'b')),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test that access_nested_map raises a KeyError for invalid paths.
        """
        with self.assertRaises(KeyError) as context:
            utils.access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), f"'{path[-1]}'")


class TestGetJson(unittest.TestCase):
    """
    Test cases for the get_json function.
    """

    @parameterized.expand([
        ('http://example.com', {"a": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Test that get_json returns the expected payload from a given URL.
        """
        with patch('utils.requests.get') as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            result = utils.get_json(test_url)

            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """
    Test cases for the memoize decorator.
    """

    def test_memoize(self):
        """
        Test that memoize caches the result of a method call.
        """

        class TestClass:
            def a_method(self):
                return 42

            @utils.memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass,
                          'a_method', return_value=42) as mock_method:
            test_instance = TestClass()
            result1 = test_instance.a_property
            result2 = test_instance.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
