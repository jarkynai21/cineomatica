from django.test import TestCase

from django.test import TestCase
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

class TestCinemaApi(APITestCase):

    @classmethod
    def setUp(cls):
        cls.user = User.objects.create_superuser(username='jarkynai', password='jaja96')

    def test_cinema_api(self):
        self.client.login(username='jarkynai', password='jaja96')

        url = '/api/cinema/'

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_cinema_add_api(self):
        self.client.login(username='jarkynai', password='jaja96')

        url = '/api/cinema/'

        data = {
            'title': 'Kosmo Park',
            'schedule': 'all day',
            'address': 'Ynusalieva',
            'contact': "0700345612",

        }
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_cinema_delete_api(self):
        self.client.login(username='jarkynai', password='jaja96')

        url = '/api/cinema/'

        data = {
            'title': 'Kosmo Park',
            'schedule': 'all day',
            'address': 'Ynusalieva',
            'contact': "0700345612",
        }

        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, 201)


    def test_cinema_update_api(self):
        self.client.login(username='jarkynai', password='jaja96')

        url = '/api/cinema/'

        data = {
            'title': 'Kosmo Park',
            'schedule': 'all day',
            'address': 'Ynusalieva',
            'contact': "0700345612",
        }

        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, 201)
