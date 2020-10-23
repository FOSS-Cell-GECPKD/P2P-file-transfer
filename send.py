import socket
from _thread import *
import os
from requests import get
import urllib.request


def get_ip():
    ip=socket.gethostname()
    print("Host name:"+ip)
    try:
        ip = get('https://api.ipify.org').text
        print("Your external ip :"+ip)
    except:
        print("No internet access")
    try:
        ip=([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] 
        if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), 
        s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, 
        socket.SOCK_DGRAM)]][0][1]]) if l][0][0])
        print("Local ip:"+ip)
    except:
      print("Not connected to any network")

      
def end_connection(conn):
    try:
        print("Disconnected ")
        conn.close()
    except:
        print("Connect to another")
        ans=input(str(("\nY-Yes N-No->")))
        if(ans =='y' or ans == 'Y'):
            socket_connection()
        elif(ans =='N' or ans == 'n'):
            print("Exiting server")
            exit()

        
def choose_file(conn,addr,s):
            filename=input(str("Please enter the path of the file : "))
            try:
                conn.send(filename.encode())
                print("Send filename")
                size = os.path.getsize(filename)
                size=str(size)
                conn.send(size.encode())
                ans = conn.recv(1024)
                ans = str(ans.decode())
                if(ans == 'N'):
                    print("Ending connection")
                    end_connection(conn)
                if(ans =='Y'):
                    with open(filename, 'rb') as file:
                        chunk_size=1024
                        chunk_file=file.read(chunk_size)
                        while len(chunk_file)>0:
                            conn.send(chunk_file)
                            chunk_file=file.read(chunk_size)
                    file.close()
                    print("Data has been transmitted successfully")
                    ans = conn.recv(1024)
                    ans = str(ans.decode())
                    if ans=="Y" or ans=="y":
                        choose_file(conn,addr,s)
                    else:
                        print("!!Exiting!!")
                        end_connection()
            except:
                print("Do you want to try again?")
                ans=input(str(("\nY-Yes N-No->")))
                if(ans =='y' or ans == 'Y'):
                    choose_file(conn,addr,s)
                elif(ans =='N' or ans == 'n'):
                    print("Closing connection")
                    end_connection()

                    
def socket_connection():
    try:
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port=8080
        s.bind(('',port))

        s.listen(10)
        print("Waiting for a connection")
        conn, addr =s.accept()
        
        print(addr, "has connected to the system")
        
        choose_file(conn,addr,s)
    except:
        print("Connection error")
        print("Do you want to try again?")
        ans=input(str(("\nY-Yes N-No->")))
        if(ans =='y' or ans == 'Y'):
            socket_connection()
        elif(ans =='N' or ans == 'n'):
            print("Exiting server")
            exit()

            
def send_file():
    get_ip()
    socket_connection()
    
    
