import hashlib 
from pathlib import Path
from cryptography.fernet import Fernet
import os

def hash_file(filename):
   # make a hash object
   h = hashlib.sha256()

   # open file for reading in binary mode
   with open(filename,'rb') as file:

       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           chunk = file.read(1024)
           h.update(chunk)

   return h.hexdigest()


def file_size(file):
    return str(Path(file).stat().st_size/1000)+'KB'


def encrypt(file_name):
    key=Fernet.generate_key()
    f = Fernet(key)
    with open(file_name, "rb") as file:
        # read all file data
        file_data = file.read()
    
    encrypted_data = f.encrypt(file_data)
    # write the encrypted file
    with open(file_name+'.AES', "wb") as file:
        file.write(encrypted_data)
    os.remove(file_name)
    return key


def decrypt(file_name, key):
    f = Fernet(key)
    with open(file_name, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open('ORG.'+file_name[:-3], "wb") as file:
        file.write(decrypted_data)
    os.remove(file_name)


    
