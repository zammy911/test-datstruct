from django.test.client import Client
from profile.models import * 
from django.test import TestCase
from tddspry.django import TestCase as TddspryTestCase
from django.contrib.auth.models import User


class ContactTestCase(TestCase):
    """ Test to check if data is loaded from fixtures """

    def setUp(self):
        self.count = Contact.objects.count()

    def testFixtures(self):
        self.assertEqual(self.count, 1)


class LoginTestCase(TestCase):
    """ Test if page redirects to login """

    def test_redirect_to_login(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 302)
    
    def test_login(self):
        user = User.objects.create_user('john', 'lennon@thebeatles.com', 'john')
        user.save() 
        response = self.client.post('/accounts/login/', {'username': 'john', 'password': 'john'})
        self.assertEqual(response.status_code, 302)
        response = self.client.get("/")   
        # check if page has info from fixtures
        self.assertNotEqual(response.content.find('Zamkovoi'), -1)


class DbLogTestCase(TestCase):
    """ Test if sql queries are logged to db  """
   
    def test_db_logging(self):
        queries_num = DbLog.objects.count()
        response = self.client.get("/admin/")
        queries_num2 = DbLog.objects.count()
        self.assertNotEqual(queries_num, queries_num2)
        query = DbLog.objects.filter().order_by('-added')[0]
        self.assertNotEqual(unicode(query.sql).find('site'), -1)
