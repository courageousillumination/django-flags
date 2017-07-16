"""Tests for the flag class."""
from unittest import TestCase

from flags.flag import Flag, FlagType


class FlagTestCase(TestCase):
    """Tests around the flag set."""

    def setUp(self) -> None:
        self.flag = Flag.create_from_config({
            'name': 'test',
            'flag_type': 'int',
            'default_value': 0
        })

    def test_create_from_config(self) -> None:
        """Make sure we can create a Flag from a configuration dictionary."""
        self.assertEqual(self.flag.name, 'test')
        self.assertEqual(self.flag.flag_type, FlagType.INT)
        self.assertEqual(self.flag.default_value, 0)

    def test_cast_string_int(self) -> None:
        """Make sure we can cast an string to an int."""
        self.assertEqual(self.flag.cast_string('42'), 42)

    def test_cast_string_failure(self) -> None:
        """Make sure we fail loudly if a cast fails."""
        self.flag.flag_type = None
        self.assertRaises(ValueError, self.flag.cast_string, '42')
