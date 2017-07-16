"""Tests for the FlagSet and related utilites."""
from unittest import TestCase

from flags.flag_set import FlagSet
from flags.flag_overrider import FlagOverrider

class SimpleOverrider(FlagOverrider):
    """A simple overrider that always return 42."""

    def should_override(self, flag, **kwargs):
        """Yes."""
        return True

    def get_override(self, flag, **kwargs):
        """The answer."""
        return 42

class FlagSetTestCase(TestCase):
    """Tests around the flag set."""

    FLAG_CONFIG = [{
        'name': 'int_flag',
        'flag_type': 'int',
        'default_value': 0
    }]

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
        flag_set = FlagSet.create_from_config(self.FLAG_CONFIG, [SimpleOverrider()])
        self.assertEqual(flag_set.get_flag_value('int_flag'), 42)
