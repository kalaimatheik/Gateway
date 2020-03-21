import hashlib 
from pathlib import Path

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


x=hash_file('bugs.txt')
print(x)


def file_size(file):
    return str(Path(file).stat().st_size/1000)+'KB'

x=file_size('data.sql')
print(x)