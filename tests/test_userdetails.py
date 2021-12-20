'''
@author: Dibyesh Mishra
@date: 20-12-2021 21:22
'''
import unittest
from  user_registration_exception import  UserRegistrationException
from  validation import  UserDetails

class TestUserDetails(unittest.TestCase):
    def test_user_first_name(self):
        param = "Alex"
        user = UserDetails()
        user.set_first_name(param)
        self.assertEqual(param, user.get_first_name())

    def test_user_first_name_if_invalid(self):
        param = "alex"
        user = UserDetails()
        try:
           user.set_first_name(param)
        except UserRegistrationException as exception:
            self.assertEqual("first name is invalid", exception.__str__())

    def test_user_first_name_if_empty(self):
        param = ""
        user = UserDetails()
        try:
            user.set_first_name(param)
        except UserRegistrationException as exception:
            self.assertEqual("name can not be empty", exception.__str__())

    def test_user_phone_number(self):
        param = "91 2345678902"
        user = UserDetails()
        user.set_phone_no(param)
        self.assertEqual(param, user.get_phone_no())

    def test_user_phone_number_if_invalid(self):
        param = "8900388290"
        user = UserDetails()
        try:
            user.set_phone_no(param)
        except UserRegistrationException as exception:
            self.assertEqual("Invalid phone number", exception.__str__())

    def test_user_phone_number_if_empty(self):
        param = ""
        user = UserDetails()
        try:
            user.set_phone_no(param)
        except UserRegistrationException as exception:
            self.assertEqual("phone_no can not be empty", exception.__str__())

    def test_user_email_id(self):
        param = "abc@gmail.com"
        user = UserDetails()
        user.set_email(param)
        self.assertEqual(param, user.get_email())

    def test_user_email_id_if_invalid(self):
        param = "ajkkskA@gmail"
        user = UserDetails()
        try:
            user.set_email(param)
        except UserRegistrationException as exception:
            self.assertEqual("Invalid email id", exception.__str__())

    def test_user_email_id_if_empty(self):
        param = ""
        user = UserDetails()
        try:
            user.set_email(param)
        except UserRegistrationException as exception:
            self.assertEqual("email_id can not be empty", exception.__str__())
