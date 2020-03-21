import hashlib

def hash_file(filename):
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


#print(hash_file('data.sql'))