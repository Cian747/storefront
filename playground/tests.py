from django.test import TestCase
from django.contrib.auth.models import User
from .models import Customer,Category,Order, Products

# Create your tests here.

class AppTestCase(TestCase):
    
    def setup(init):
        '''
        Create an test all your classes before you work on the application logic
        '''

