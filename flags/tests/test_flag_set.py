"""Tests for the FlagSet and related utilites."""
from unittest import TestCase

from flags.flag_set import FlagSet


class FlagSetTestCase(TestCase):
    """Tests around the flag set."""

    def test_empty_config(self) -> None:
        """Make sure we can create a FlagSet from a configuration array."""
        flag_set = FlagSet.create_from_config([])
        self.assertIsInstance(flag_set, FlagSet)

    def test_single_flag(self) -> None:
        """Make sure we can load up a flag from a definition."""
        flag_set = FlagSet.create_from_config([{
            'name': 'test_flag',
            'flag_type': 'int',
            'default_value': 0
        }])
        self.assertIsNotNone(flag_set.get_flag('test_flag'))
