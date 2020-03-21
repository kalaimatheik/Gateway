import pyAesCrypt
import random
from cryptography.fernet import Fernet

sub_key="abcdefg!~hijklm#$&*nopqrstuvw-+@xyz02345+/67890A-)(%BCDEFGHIJKLMNOPQRSTUVWXYZ"
enc_key =  "".join(random.sample(sub_key,50))
key=Fernet.generate_key()

print(enc_key,key)

'''
# decrypt
with open("data.txt.aes", "rb") as fIn:
    try:
        with open("dataout.txt", "wb") as fOut:
            # decrypt file stream
            pyAesCrypt.decryptStream(fIn, fOut, password, bufferSize, encFileSize)
    except ValueError:
        # remove output file on error
        remove("dataout.txt")


        '''