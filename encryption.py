import hashlib 
import pyAesCrypt
import random
from os import stat, remove
from pathlib import Path

sub_key="abcdefg!~hijklm#$&*nopqrstuvw-+@xyz02345+/67890A-)(%BCDEFGHIJKLMNOPQRSTUVWXYZ"

bufferSize = 64 * 1024

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

def hash_db(filename):
   # make a hash object
   h = hashlib.sha3_512()

   # open file for reading in binary mode
   with open(filename,'rb') as file:

       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           chunk = file.read(1024)
           h.update(chunk)

   return h.hexdigest()   


def file_size(file):
    return 


def encrypt(file_name):
    key =  "".join(random.sample(sub_key,50))
    try:
        pyAesCrypt.encryptFile(file_name, file_name+'.AES', key, bufferSize)
        fsize=str(Path(file_name).stat().st_size/1000)+'KB'
        os.remove(file_name)
        print('''----------Encryption Sucessfull----------\n \nUser Warning: Make sure to notedown the encryption key,
	failure to do so the data cannot be reverted back ever again.''')
        print('\nEncryption Key: ',enc_key+'\n')
        now=time.strftime("%H:%M")
        with open('C:\\Intel\\'+'temp_key.txt','a+') as f:
            f.write(file_name+'|||'+now+'||||'+key+'\n')
        time.sleep(10)
        return file_name,fsize,key
    except:
        return False

file_name="C:\Users\rexdi\Desktop\MongoDB with Python Crash Course - Tutorial for Beginners - YouTube.mkv"
encrypt(file_name)

def decrypt(file_name,key):
    try:
        pyAesCrypt.encryptFile(file_name,'Decrypt_'+file_name, key, bufferSize)
        os.remove(file_name)
        return True
    except:
        return False

