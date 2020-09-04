"""
contains all user methods

"""

class User:
    """empty dictionary to store users as they have usernames and passwords"""
    users = {}
    
    
    @staticmethod
    def add_user(key, value):
        User.users.update({key: value})
     
    @staticmethod    
    def user_login(k, val):
          for key, value in User.users.items():
              if k == key and val == value:
                  return "Login Successful"
              else:
                  return "Login failed" 

    @staticmethod
    def del_user(val):
        for value in User.users.items():
            if val == value:
                User.users[value].pop()
            else:
                return "failed"    
                    
    def __init__(self, name, password):
      self.name = name
      self.password = password    
    