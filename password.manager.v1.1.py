#Password Manager - DO NOT STORE REAL PASSWORDS HERE, NOT SECURE

from cryptography.fernet import Fernet

'''def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)  '''     


def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key


key = load_key() 
fer = Fernet(key)


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = (line.rstrip())
            acc, user, passw = data.split("|")
            print('Account: ', acc, '|', 'Username: ', user, "|", "Password: ", fer.decrypt(passw.encode()).decode())
def add():
    acc_name = input("Account Name: ")
    user_name = input('User name: ')
    pwd = input('Password: ')

    with open('passwords.txt', 'a') as f:
        f.write(acc_name + '|' + user_name + '|' + fer.encrypt(pwd.encode()).decode() + '\n')


while True:

    mode = input("Would you like to add a password or view existing? (view/add) Press q to quit. ").lower()
    
    if mode == 'q':
        break

    elif mode == 'view':
        view()
        
    elif mode == 'add':    
        add()
        
    else:
        print('Not a valid answer.')
        continue

else:
    quit() 
