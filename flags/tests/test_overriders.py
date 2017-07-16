"""Tests for the basic overriders provided by the flags app."""
from django.test import TestCase

from flags.flag import Flag
from flags.models import SiteFlagOverride
from flags.overriders import SiteFlagOverrider


class SiteFlagOverriderTestCase(TestCase):
    """Tests for the SiteFlagOverrider."""

    def setUp(self):
        self.flag = Flag(name='test_flag', flag_type='int', default_value=0)
        self.overrider = SiteFlagOverrider()

    def test_checks_existence(self) -> None:
        """Make sure we only try to override if an override exists."""
        self.assertFalse(self.overrider.should_override(self.flag))
        SiteFlagOverride.objects.create(name='test_flag', value='10')
        self.assertTrue(self.overrider.should_override(self.flag))

    def test_applies_override(self) -> None:
        """Make sure we properly apply a site wide override."""
        SiteFlagOverride.objects.create(name='test_flag', value='10')
        self.assertEqual(self.overrider.get_override(self.flag), 10)
