"""Tests for the FlagSet and related utilites."""
from unittest import TestCase

from flags.flag_set import FlagSet
from flags.tests.overriders import NeverOverride, SimpleOverrider


class FlagSetTestCase(TestCase):
    """Tests around the flag set."""

    FLAG_CONFIG = [{'name': 'int_flag', 'flag_type': 'int', 'default_value': 0}]

    def setUp(self) -> None:
        self.flag_set = FlagSet.create_from_config(self.FLAG_CONFIG)

    def test_empty_config(self) -> None:
        """Make sure we can create a FlagSet from a configuration array."""
        flag_set = FlagSet.create_from_config([])
        self.assertIsInstance(flag_set, FlagSet)

    def test_single_flag(self) -> None:
        """Make sure we can load up a flag from a definition."""
        self.assertIsNotNone(self.flag_set.get_flag('int_flag'))

    def test_get_default_value(self) -> None:
        """Make sure that intially we get the default value of a flag."""
        self.assertEqual(self.flag_set.get_flag_value('int_flag'), 0)

    def test_with_single_overrider(self) -> None:
        """Make sure that the flag set properly applies overriders."""
        flag_set = FlagSet.create_from_config(self.FLAG_CONFIG, [SimpleOverrider(42)])
        self.assertEqual(flag_set.get_flag_value('int_flag'), 42)

    def test_multiple_overriders(self) -> None:
        """Make sure that overriders have a precedence."""
        flag_set = FlagSet.create_from_config(self.FLAG_CONFIG,
                                              [SimpleOverrider(13),
                                               SimpleOverrider(42)])
        self.assertEqual(flag_set.get_flag_value('int_flag'), 13)

    def test_overrider_fall_thorugh(self) -> None:
        """Make sure we fall though the overriders in order."""
        flag_set = FlagSet.create_from_config(self.FLAG_CONFIG,
                                              [NeverOverride(),
                                               SimpleOverrider(42)])
        self.assertEqual(flag_set.get_flag_value('int_flag'), 42)

    def test_allows_iteration(self) -> None:
        """Make sure we can iterate over a flagset."""
        count = 0
        for _ in self.flag_set:
            count = +1
        self.assertEqual(count, 1)
