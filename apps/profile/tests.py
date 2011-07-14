from django.test.client import Client
from profile.models import * 
from django.test import TestCase
from tddspry.django import TestCase as TddspryTestCase
from django.conf import settings

class ContactTestCase(TestCase):
    """ Test to check if data is loaded from fixtures """

    def setUp(self):
        self.count = Contact.objects.count()

    def testFixtures(self):
        self.assertEqual(self.count, 1)


class MainPageTestCase(TestCase):
    """ Test to check if main page is here """

    def setUp(self):
        self.client = Client()

    def test_main_page(self):
        response = self.client.get('/')
        # check if page exists
        self.assertEqual(response.status_code, 200)
        # check if page has info from fixtures
        self.assertNotEqual(response.content.find('Zamkovoi'), -1)

