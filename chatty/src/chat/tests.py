from django.test import TestCase
from chat.models import Message
# Create your tests here.

class MessageTestCase(TestCase):
    def setup(self):
        Message.Objects.create(username='ldminh2', room='test', content='abcxyz')

    def test(self):
        Message.Objects.create(username='ldminh2', room='test', content='abcxyz')
        self.assertEqual(1, 1)