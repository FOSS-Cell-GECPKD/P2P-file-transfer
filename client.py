import socket
import os
from requests import get
ip = get('https://api.ipify.org').text
print("Your external ip :"+ip)
s=socket.socket()
host=input(str("Enter the host address of the senter : "))
port=8080
s.connect((host,port))
print(" Connected to the host... ")
filename=input(str("please enter a filename for the incoming file : "))
filesize = str(s.recv(10))
filesize=int(filesize[2:-1])
print (filesize)
print(type(filesize))
with open(filename, 'wb') as file:
    chunk_size=1024
    chunk_file=s.recv(chunk_size)
    file.write(chunk_file)
    totalrecv=len(chunk_file)
    while totalrecv<filesize:
        chunk_file=s.recv(chunk_size)
        file.write(chunk_file)
        totalrecv+=len(chunk_file)
        if (int(totalrecv*100/filesize)%10 == 0):
            print(totalrecv*100/filesize)
file.close()

print("File has been recived.")



