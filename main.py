from otp import key
from PIL import Image
from database import login_name,login_pas,login_lock,verify_lock,login_unlock


def login():
    c=0
    while True:
        usr=input('UserName: ')
        if usr==login_name(usr):
            pas=input('Password: ')
            if usr==login_name(usr) and pas==login_pas(usr) and verify_lock(usr)=='A':
                print('Login Successful')
                otp_key=input('Enter the OTP: ')
                if otp_key==key():
                    print('OTP Verified')
                    return 1
                else:
                    print('Invalid OTP')
            elif usr==login_name(usr) and pas==login_pas(usr) and verify_lock(usr)=='D':
                print('Account is locked... Contact ADMIN')
                return 0
            else:
                print('Incorrect Credentials Try Again!')   
            c+=1
            if c==3:
                print('Too many attempts... Account is locked')
                login_lock(usr)
                return -1
        else:
            print('Invalid Username')
            return 999

def new_login():
    usr=input('Enter Username: ')
    pas=input('Enter Password: ')
    pas_re=input('Re Enter the password: ')
    im=Image.open('otp.png')
    im.show()
    op=input('Sync the OTP for validation: ')

def db_unlock():
    ip=input('Enter the OTP + 4 digit pin: ')
    print(key()+'1604',str(ip)+'1604')
    if key()+'1604'==str(ip):
        usr=input('Enter the username to be unlocked: ')
        print(login_unlock(usr))
        if usr==login_name(usr):
            login_unlock(usr)
            print('Account Unlocked: ',usr)
            return 1
        else:
            print('Invalid User Name')
            return 0
        return 1

db_unlock()
    