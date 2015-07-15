from django.test import TestCase
from .models import Device, User
from www.repositories.user_repository import UserRepository

class DeviceTestCase(TestCase):
    fixtures = ['www_testdata.yaml']

    def test_device_can_be_reserved_by_a_user(self):
        device = Device.objects.first() # get a sample device
        user = User.objects.first() # get a sample user

        device.reserve(user) # reserve device for this user

        assert device.reserved_by.email == 'mrosati@h-art.com'
        assert user.device_set.first().serial_number == 'H-ART 2012 2736000000K'

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

    def test_it_can_filter_using_last_name(self):
        ur = UserRepository()

        users = ur.get_by_last_name('bu') # only 1 result

        self.assertEqual(len(users), 1)

        users = ur.get_by_last_name('ti') # this gets 2 results

        # order matters
        self.assertEqual(len(users), 2)
        self.assertEqual(users[0].email, 'rbutti@h-art.com')
        self.assertEqual(users[1].email, 'mrosati@h-art.com')
