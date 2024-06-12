from cryptography.fernet import Fernet

#key + password + text to encrypt = random text
"""def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
write_key()"""

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

#if you wanna get master_pwd activated, you need more complex code
#The document is in the description below!
master_pwd = input('What is the master password?: ')
#To add master_pwd to key, you gotta convert bit to bytes by .byte or .encode()
key = load_key() + master_pwd.encode()
fer = Fernet(key)

def add():
    name =input("Account Name: ")
    pwd = input("Password: ")

    #a = pend mode: if file not exist create file with defined name and write and read it
    with open("password.txt","a") as f: 
        f.write(name + "|" +fer.encrypt(pwd.encode()).decode() + '\n')


def view():
    with open("password.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            if '|' in data:
                user, passw = data.split('|', 1)  # Split on the first occurrence of '|'
                print("User:", user, "|", "Password:", fer.decrypt(passw.encode()).decode())
            else:
                print("Invalid format:", data)



while True:
    mode = input("Would you like to add a new password or view existing ones(add/view) or press q to quit: ").lower()

    if mode == "q":
        break

    if mode =='add':
        add()
    elif mode == 'view':
        view()
    else:
        print("Invalid mode.")
        continue




