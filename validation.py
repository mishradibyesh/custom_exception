"""
generating custom exception  using try except
"""
import re
from user_registration_exception import UserRegistrationException


class Validation:

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, first_name):
        if re.fullmatch("^[A-Z]{1}[a-z]{3,}$", first_name):
            self.first_name_ = first_name
            print(first_name)
        else:
            raise UserRegistrationException("first name is invalid")


first_name = input("enter the first name : ")
validate = Validation()
try:
    validate.set_first_name(first_name)
except UserRegistrationException as exception:
    print(exception.__str__())
finally:
    print("finally block executed")
