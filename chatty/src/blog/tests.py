from django.test import TestCase
from .models import CustomUser
# Create your tests here.
class DatabaseTestCase(TestCase):
    def setUp(self):
        username = 'ldminh3'
        password = '123456'
        CustomUser.objects.create_user(username=username,password=password)

    def test_first_test(self):

        user = CustomUser.objects.filter(username='ldminh')
        print(user)
        self.assertEqual(1,1)
