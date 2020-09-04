import random
import string

class PasswordManager:
    """
    class for the passwords
    """
    
    passwords_list = []
    
    def __init__(self, name, password):
      self.name = name
      self.password = password
    
    def save_password(self):
        PasswordManager.passwords_list.append(self)
        
    def delete_password(self):
        PasswordManager.passwords_list.remove(self)
        
    @classmethod
    def display_passwords(cls):
        return cls.passwords_list
    
    @staticmethod
    def find_by_name(appName):
        for password in PasswordManager.passwords_list:
            if password.name == appName:
                return password
    
    @staticmethod
    def generate_password():
        letters = string.ascii_letters
        result_str = ''.join(random.choice(letters) for i in range(10))
        password =  result_str
        
        return password
             