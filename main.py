from otp import key
from PIL import Image
from database import login_name,login_pas,login_lock,verify_lock,login_unlock,verify_lock,admin_check,new_user
from uuid import uuid4
from encryption import encrypt,decrypt,hash_file,hash_db
import time


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
    im=Image.open('otp.png')
    im.show()
    x=1
    while True:
        op=input('Sync the OTP for validation: ')
        if op==key():
            print('OTP Verified...please wait profile is being created....')
            time.sleep(3)
            pin=(input('Please give a 4 digit PIN: '))
            tkn=str(uuid4())
            new_user(usr,pas,pin,tkn)
            break
        else:
            print('Invalid OTP')
    


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



def security():
    db='data.sql'
    hash='3b6f51a6e1fddf586ae3d24d62039c2c2609e1c084a1cd7de39470083e1002c36768f2f9f9a0a696c729caa4053b1f9b40a8335023ec3f24435c07ac614250cb'

    if hash_db(db)==hash:
        return True
    else:
        return False

def file_access(file):
    ip=int(input('1.Encryption\n2.Decryption\n3.Keys\n4.Hash_files\nChoose Options to manage files: '))
    if ip==1:
        path=input('Input File Path: ')
        stats=encrypt(file)
        if stats==False:
            print('Invalid Path')
        else:
            print(file,stats)
    

