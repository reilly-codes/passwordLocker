"""
contains all user methods

"""

class User:
    """empty dictionary to store users as they have usernames and passwords"""
    users = []
    
    
    def add_user(self):
        User.users.append(self)

    def del_user(self):
        User.users.remove(self)  
                    
    def __init__(self, name, password):
      self.name = name
      self.password = password    
    