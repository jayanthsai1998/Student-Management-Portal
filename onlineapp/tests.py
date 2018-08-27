from django.test import TestCase

# Create your tests here.

import unittest
from onlineapp.models import *
from onlineapp.serializers import  *


class CollegeSerializerTest(TestCase):
    #def test_CollegeSerializer(self):
    def setup(self):
        self.college = College.objects.create(name= 'Gayathri Vidhya Parishad' , location = 'Vizag', acronym = 'GVP', contact = 'contact@gvp.edu')
        self.serializer = CollegeSerializer(self.college)

    def test_college_valid_serialize(self):
        self.assertEqual(self.serializer.data, { 'name' : 'Gayathri Vidhya Parishad' , 'location' : 'Vizag', 'acronym' : 'GVP', 'contact' : 'contact@gvp.edu' })

    def test_college_invalid_serialize(self):
        self.assertNotEqual(self.serializer.data, { 'name' : 'Gayathri Vidhya Parishad College' , 'location' : 'Visakha', 'acronym' : 'GVPE', 'contact' : 'contact@gvpe.edu' })


