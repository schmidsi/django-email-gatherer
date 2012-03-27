from datetime import datetime

from django.utils import unittest

from .models import GatheredEmail


class SimpleTestCase(unittest.TestCase):
    def test_creation(self):
        new_gathering = GatheredEmail(email='asdf@asdf.com')
        new_gathering.save()
        self.assertEqual(GatheredEmail.objects.get(email='asdf@asdf.com'), new_gathering)


class CreatedExtensionTestCase(unittest.TestCase):
    def setUp(self):
        GatheredEmail.register_extensions('created')
        self.assertTrue('created' in [ field.name for field in GatheredEmail._meta.fields ])

    def test_created(self):
        new_gathering = GatheredEmail(email='created-test@asdf.com')
        new_gathering.save()
        self.assertTrue(hasattr(new_gathering, 'created'))
        self.assertTrue(new_gathering.created < datetime.now())
