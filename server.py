import socket
import os

s=socket.socket()
host=socket.gethostname()
port=8080
s.bind((host,port))
s.listen(1)
print("Host name is: ")
print(host)
print("Waiting for a connection")
conn, addr =s.accept()
print(addr, "has connected to the system")
filename=input(str("Please enter the filename of the file : "))
conn.send(filename.encode())
size = os.path.getsize(filename)
size=str(size)
conn.send(size.encode())
with open(filename, 'rb') as file:
    chunk_size=1024
    chunk_file=file.read(chunk_size)
    while len(chunk_file)>0:
        conn.send(chunk_file)
        chunk_file=file.read(chunk_size)
        
"""file=open(filename,'rb')
file_data=file.read(25*1024)
conn.send(file_data)"""

print("Data has been transmitted successfully")
