import socket
import os
from requests import get
def yesorno(s):
    ans=input(str(("\nY-Yes N-No->")))
    if(ans =='y' or ans == 'Y'):
        ans='Y'
        s.send(ans.encode())
        file(s)
    elif(ans =='N' or ans == 'n'):
        ans = 'N'
        s.send(ans.encode())
        s.close()
def connection():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        host=input(str("Enter the host address of the senter : "))
        port=8080
        s.connect((host,port))
        print(" Connected to the host... ")
        return s
    except:
        print("Connection error do you want to try again?")
        ans=input(str(("\nY-Yes N-No->")))
        if(ans =='y' or ans == 'Y'):
            file(connection())
        elif(ans =='N' or ans == 'n'):
            exit()
def file(s):
    filename=s.recv(1024)
    filename=filename.decode()
    filename=os.path.basename(filename)
    filesize=s.recv(1024)
    filesize=int(filesize.decode())
    print("Do you want to download % s of size % s" % (filename, filesize))
    ans=input(str(("\nY-Yes N-No->")))
    if(ans =='y' or ans == 'Y'):
        ans = 'Y'
    elif(ans =='N' or ans == 'n'):
        ans = 'N'
    s.send(ans.encode())
    if(ans =='Y'):
        filename = "Recived"+filename
        with open(filename, 'wb') as file:
            chunk_size=1024
            chunk_file=s.recv(chunk_size)
            file.write(chunk_file)
            totalrecv=len(chunk_file)
            while totalrecv<filesize:
                chunk_file=s.recv(chunk_size)
                file.write(chunk_file)
                totalrecv+=len(chunk_file)
                print(totalrecv*100/filesize)
        
        file.close()

        print("File has been recived.")
    else:
        print("!!Exiting!!")
    print("Do yo want to continue?")
    yesorno(s)
def receive_file():
    file(connection())
