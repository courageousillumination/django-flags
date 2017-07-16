"""Tests around the flags utilites."""

import json
from io import StringIO
from unittest.mock import MagicMock, patch

from django.test import TestCase, override_settings

from flags.flag_set import FlagSet
from flags.tests.overriders import SimpleOverrider
from flags.utils import get_flag_set, get_flag_value, get_overriders, load_flag_set


class UtilsTestCase(TestCase):
    """Tests around the Utility functions."""

    FLAG_SET_CONFIG = '[{"name": "test_flag", "flag_type": "int", "default_value": 0}]'

    @override_settings(FLAGS_OVERRIDERS=['flags.tests.overriders.SimpleOverrider'])
    def test_get_overriders(self) -> None:
        """Make sure we can get the overriders from the django settings."""
        overriders = get_overriders()
        self.assertEqual(len(overriders), 1)
        self.assertIsInstance(overriders[0], SimpleOverrider)

    def test_load_flag_set(self) -> None:
        """Make sure we can load a flag set from a file."""
        fake_file = StringIO(self.FLAG_SET_CONFIG)
        flag_set = load_flag_set(fake_file)
        self.assertIsInstance(flag_set, FlagSet)
        self.assertEqual(flag_set.get_flag_value('test_flag'), 0)

    @patch('flags.utils.load_flag_set_path')
    @override_settings(FLAGS_CONFIG_FILE='foobar')
    def test_get_flag_set(self, patched_load: MagicMock) -> None:
        """Make sure the flag set loads from the correct location."""
        flag_set = get_flag_set()
        patched_load.assert_called_with('foobar')
        self.assertIsNotNone(flag_set)

    @patch('flags.utils.get_flag_set')
    def test_get_flag_value(self, patched_get: MagicMock) -> None:
        """Make sure we can get a flag value."""
        patched_get.return_value = FlagSet.create_from_config(json.loads(self.FLAG_SET_CONFIG))
        self.assertEqual(get_flag_value('test_flag'), 0)
