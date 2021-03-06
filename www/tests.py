import json
from django.test import Client, TestCase
from .models import Device, User
from www.repositories.user_repository import UserRepository

class DeviceTestCase(TestCase):
    fixtures = ['www_testdata.yaml']

    def setUp(self):
        client = Client()
        client.login(username='admin', password='admin')

    def test_device_can_be_reserved_by_a_user(self):
        device = Device.objects.first() # get a sample device
        user = User.objects.first() # get a sample user

        device.reserve(user) # reserve device for this user

        self.assertEqual(device.reserved_by.email, 'user1@companyname.com')
        self.assertEqual(user.device_set.first().serial_number, 'DEV-ID 2012 2736000000K')

    def test_device_has_method_to_check_if_its_reserved(self):
        device = Device.objects.first() # get a sample device
        user = User.objects.first() # get a sample user

        assert device.is_reserved() is False

        device.reserve(user) # reserve device for this user

        assert device.is_reserved() is True # now device is reserved

    def test_reserved_device_can_be_set_free(self):
        device = Device.objects.first() # get a sample device
        user = User.objects.first() # get a sample user

        device.reserve(user) # reserve device for this user

        device.set_free() # set the device free

        assert device.reserved_by is None

class UserRepositoryTestCase(TestCase):
    fixtures = ['www_testdata.yaml']

    def setUp(self):
        client = Client()
        client.login(username='admin', password='admin')

    def test_it_can_filter_using_last_name(self):
        ur = UserRepository()

        users = ur.get_by_last_name('bu') # only 1 result

        self.assertEqual(len(users), 1)

        users = ur.get_by_last_name('ti') # this gets 2 results

        # order matters
        self.assertEqual(len(users), 2)
        self.assertEqual(users[0].email, 'user4@companyname.com')
        self.assertEqual(users[1].email, 'user1@companyname.com')

class SiteFunctionalTestCase(TestCase):
    fixtures = ['www_testdata.yaml']

    def setUp(self):
        self.client = Client()

    def test_user_cannot_get_the_home_page_as_anonymous(self):
        response = self.client.get('/')

        # user is redirected to login page
        self.assertEqual(response.status_code, 302)

        self.client.login(username='admin', password='admin')

        response = self.client.get('/')

        # user is authenticated now, should get 200
        self.assertEqual(response.status_code, 200)

    def test_user_can_autocomplete_users_last_name(self):
        self.client.login(username='admin', password='admin')

        response = self.client.get('/users/', {'last_name': 'r'})

        json_response = json.loads(response.content)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json_response['suggestions']), 2)
