from user import User
from credential import PasswordManager

def create_user(User_name, User_password):
    new_user = User(User_name, User_password)
    return new_user

def save_user(user):
    user.add_user()
    
def delete_user(user):
    user.del_user()
    
def add_pass(app_name, app_password):
    new_password = PasswordManager(app_name, app_password)
    return new_password

def save_pass(password):
    password.save_password()
    
def find_password(appName):
    return PasswordManager.find_by_name(appName)

def display_pass():
    return PasswordManager.display_passwords()

def del_password(appName):
    appName.delete_password()
    
def gen_pass():
    return PasswordManager.generate_password()
 
def main():
    print(" " + "|" + "  " + "|" + " " + "|")
    print(" " + "|" + "--" + "|" + " " + "|")
    print(" " + "|" + "  " + "|" + " " + "|")
    print('\n')
    print("Kindly create Account")
    print('\n')
    print("Enter your desired user name : ")
    Username = input()
    print("Enter you desired login password : ")
    Userpassword = input()
    
    save_user(create_user(Username, Userpassword))
    
    print('*'*10)
    print(f"{Username} Account successfully created")
    print('\n')
    print('-'*20)

    while True:
        print("Use these short codes : cp - to create password, dp - display passwords, fp - find password, dd - delete password, ex - exit program,")
        
        short_code = input().lower()
        
        if short_code == 'cp':
            print("New Password")
            print('*'*10)
            
            print("Do yo want password generated(y/n)")
            gen_option = input().lower()
            
            if gen_option == 'y':
                print("platform Name:")
                app_name = input()
                print("generating password")
                app_password = gen_pass()
            elif gen_option == 'n':  
                print("platform Name:")
                app_name = input()
                print("password:")
                app_password = input()
            else:
                print("I didn't catch that")
            
            save_pass(add_pass(app_name, app_password))
            
            print('='*10)
            print("Account Created")
            
        elif short_code == 'dp':
            if display_pass():
                print("Here is a list of all your passwords")
                print('-'*10)
                for password in display_pass():
                    print(f"{password.name} - {password.password}")
                    print('\n')
                    
        elif short_code == 'fp':
            print("Enter the name of the password you want to delete")
            search_name = input()
            if find_password(search_name):
                print("Deleted")
            else:
                print("not found")
                      
        
        elif short_code == 'dd':
            print("What password do you want to delete")
            delete_name = input()
            delete_password = find_password(delete_name)
            print('='*10)
            if delete_password:
                print(f"You have successfully delete {delete_password.name}'s password")
                del_password(delete_password)
                
        elif short_code == 'ex':
            print("bye...".upper())
            break
        
        else:
            print("Sorry I did not get That")
                
                
if __name__ == '__main__':
    main()