import socket

s=socket.socket()
host=input(str("Enter the host address of the senter : "))
port=8080
s.connect((host,port))
print(" Connected to the host... ")
filename=s.recv(1024)
filename=filename.decode()
size=s.recv(1024)
size=int(size.decode())
print("name of the file = "+filename)
print("This may take few seconds...")
with open(filename, 'wb') as file:
    chunk_size=1024
    chunk_file=s.recv(chunk_size)
    file.write(chunk_file)
    file_size=len(chunk_file)
    while file_size < size:
        chunk_file=s.recv(chunk_size)
        file.write(chunk_file)
        file_size+=len(chunk_file)
    
"""file=open(filename,'wb')
file_data=s.recv(25*1024)
file.write(file_data)
file.close()"""

print("File has been recived.")
