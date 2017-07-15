from django.test import TestCase

class SimpleTestCase(TestCase):

    def test_one_plus_one(self):
        self.assertEqual(1 + 1, 2)
