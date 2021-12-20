"""
generating custom exception  using try except
"""
import re
from user_registration_exception import UserRegistrationException


class UserDetails:
    """
    assigning the user details by checking regex statements with the help of  setter
    """

    def get_first_name(self):
        return self.first_name

    def get_phone_no(self):
        return self.phone_no

    def get_email(self):
        return self.email

    def set_first_name(self , first_name):
        """
        method to set first name of the User
        """
        if first_name == "":
            raise UserRegistrationException("name can not be empty")

        if re.fullmatch("^[A-Z]{1}[a-z]{3,}$", first_name):
            self.first_name = first_name
            print(first_name)
        else:
            raise UserRegistrationException("first name is invalid")

    def set_phone_no(self, phone_no):
        """
                method to set phone number of the User
         """
        if phone_no == "":
            raise UserRegistrationException("phone_no can not be empty")

        if re.fullmatch("^([91]{2}[ ])?[0-9]{10}$", phone_no):
            self.phone_no = phone_no
        else:
            raise UserRegistrationException('Invalid phone number')

    def set_email(self, email):
        """
                method to set email id  of the User
        """
        if email == "":
            raise UserRegistrationException("email_id can not be empty")
        if re.fullmatch(
                "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$",
                email):
            self.email = email
        else:
            raise UserRegistrationException('Invalid email id')
# first_name = input("enter the first name : ")
# validate = UserDetails()
# try:
#      validate.set_first_name(first_name)
# except UserRegistrationException as exception:
#     print(exception.__str__())
# finally:
#     print("finally block executed")
