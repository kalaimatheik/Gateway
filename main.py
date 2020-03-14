from otp import key
from PIL import Image
from database import login_name,login_pas,login_lock,verify_lock,login_unlock,verify_lock,admin_check


def login():                                                        #Login Module
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
            elif usr==login_name(usr) and pas==login_pas(usr) and verify_lock(usr)=='L':
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

def new_login():                                                #verify the login with otp sync when new id started
    usr=input('Enter Username: ')
    pas=input('Enter Password: ')
    pas_re=input('Re Enter the password: ')
    im=Image.open('otp.png')
    im.show()
    op=input('Sync the OTP for validation: ')

def db_unlock():                                                #checks for db status and enables the Admin to change its state
    usr_login=input('Enter ur usrname: ')
    usr_pas=input('Enter ur password: ')
    if usr_login==login_name(usr_login)  and usr_pas==login_pas(usr_login)  and admin_check(usr_login):
        ip=input('Enter the OTP + 4 digit pin: ')
        if key()+'1604'==str(ip):
            usr=input('Enter the username to be unlocked: ')
            if usr==login_name(usr):
                if verify_lock(usr):
                    login_unlock(usr)
                    print('Account Unlocked: ',usr)
                elif verify_lock(usr)==0:
                    print('Account Already in Unlocked State')
                else:
                    print('Invalid User Name')
                    return 0
                return 1
        else:
            print('Invalid PIN, Try Again')
    else:
        print('Incorrect Credentials')


login()