import unittest
from user import User
from credential import PasswordManager

class TestUser(unittest.TestCase):
    def setUp(self):
      self.new_user = {"Reilly":"123"}  
      
    def tearDown(self):
        User.users = {}
        
    def test_init(self):
        self.assertEqual(self.new_user.keys(),{"Reilly"})
        self.assertEqual(self.new_user["Reilly"],"123")
        
    def test_add_user(self):   
        User.add_user("Reilly", "123")
        self.assertEqual(len(list(User.users)),1)      
        
    def test_user_login(self):
        User.add_user("Reilly", "123")
        self.assertTrue(User.user_login("Reilly", "123"))
        
    def test_del_user(self):
        User.add_user("Reilly", "123")
        User.user_login("Reilly", "123")
        self.assertTrue(User.del_user("123"))    
    
    
class TestCredential(unittest.TestCase):
    def setUp(self):
        self.new_password = PasswordManager("Twitter", "123")
    
    def tearDown(self):
        PasswordManager.passwords_list = []
        
    def test_init(self):
        self.assertEqual(self.new_password.name,"Twitter")
        self.assertEqual(self.new_password.password,"123")
        
    def test_save_password(self):
        self.new_password.save_password()
        self.assertEqual(len(PasswordManager.passwords_list),1)
    
    def test_save_many_passwords(self):
        self.new_password.save_password()
        test_password = PasswordManager("Facebook", "456")
        test_password.save_password()
        self.assertEqual(len(PasswordManager.passwords_list),2)
    
    def test_delete_password(self):
        self.new_password.save_password()
        test_password = PasswordManager("Facebook", "456")
        test_password.save_password()
        self.new_password.delete_password()
        self.assertEqual(len(PasswordManager.passwords_list),1)
    
    def test_display_all_passwords(self):
        self.assertEqual(PasswordManager.display_passwords(),PasswordManager.passwords_list)
    
    def test_find_password(self):
        self.new_password.save_password()
        test_password = PasswordManager("Facebook", "456")
        test_password.save_password()
        found_password = PasswordManager.find_by_name("Facebook")
        self.assertEqual(found_password.name,test_password.name)
        
    def test_generate_password(self): 
        test = PasswordManager("Instagram", PasswordManager.generate_password())
        test.save_password()
        self.assertNotEqual(test.password, "")   
    
if __name__ == "__main__":
    unittest.main()