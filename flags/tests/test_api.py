"""Tests for the flags API."""

from unittest.mock import patch

from django.urls import reverse
from rest_framework.test import APIClient, APITestCase

from flags.flag_set import FlagSet

FLAG_CONFIG = [{
    'name': 'test1',
    'flag_type': 'int',
    'default_value': 0
}, {
    'name': 'test2',
    'flag_type': 'int',
    'default_value': 30
}]


class FlagsApiTestCase(APITestCase):
    """Tests for the Flags API."""

    def setUp(self):
        self.client = APIClient()

    @patch('flags.utils.get_flag_set')
    def test_get_all_flag_values(self, get_flag_set):
        """Make sure we can get the values of all flags."""
        get_flag_set.return_value = FlagSet.create_from_config(FLAG_CONFIG)
        results = self.client.get(reverse('flags-list')).json()
        self.assertEqual(len(results), 2)
        test1 = [x for x in results if x['name'] == 'test1'][0]
        test2 = [x for x in results if x['name'] == 'test2'][0]
        self.assertEqual(test1['value'], 0)
        self.assertEqual(test2['value'], 30)
