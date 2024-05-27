#!/usr/bin/env python3
"""test module for unittest tasks"""
import unittest
from parameterized import parameterized
import utils

class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ('a',), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)
    
    @parameterized.expand([
        ({}, ('a',)),
        ({'a': 1}, ('a', 'b')),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError) as context:
            utils.access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), f"'{path[-1]}'")

if __name__ == '__main__':
    unittest.main()