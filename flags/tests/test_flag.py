"""Tests for the flag class."""
from unittest import TestCase

from flags.flag import Flag


class FlagTestCase(TestCase):
    """Tests around the flag set."""

    def setUp(self):
        self.flag = Flag.create_from_config({'name': 'test', 'flag_type': 'int', 'default_value': 0})

    def test_create_from_config(self):
        """Make sure we can create a Flag from a configuration dictionary."""
        self.assertEqual(self.flag.name, 'test')
        self.assertEqual(self.flag.flag_type, 'int')
        self.assertEqual(self.flag.default_value, 0)
