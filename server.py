import socket
import os
from requests import get
ip = get('https://api.ipify.org').text
print("Your external ip :"+ip)
s=socket.socket()
host=socket.gethostname()
port=8080
s.bind((host,port))
s.listen(1)
print(host)
print("Waiting for a connection")
conn, addr =s.accept()
print(addr, "has connected to the system")
filename=input(str("Please enter the filename of the file : "))
conn.send(bytes(str(os.path.getsize(filename)),'utf-8'))
with open(filename, 'rb') as file:
    chunk_size=1024
    chunk_file=file.read(chunk_size)
    while len(chunk_file)>0:
        conn.send(chunk_file)
        chunk_file=file.read(chunk_size)
file.close()
print("Data has been transmitted successfully")





"""with open(filename, 'rb') as f:
    bytesToSend = f.read(1024)
    s.send(bytesToSend)
    while bytesToSend != "":
        bytesToSend = f.read(1024)
        s.send(bytesToSend)

    s.close()


    with open(filename, 'rb') as file:
    chunk_size=1024
    chunk_file=file.read(chunk_size)
    while chunk_file != "":
        conn.send(chunk_file)
        chunk_file=file.read(chunk_size)
file.close()"""
