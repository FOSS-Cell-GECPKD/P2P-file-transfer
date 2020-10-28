import os
import socket

import send
from peer import main


def open_connection():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = input(str("Enter the host address of the senter : "))
        port = 8080
        s.connect((host, port))
        print(" Connected to the host... ")
        return s
    except:
        print("Connection error do you want to try again?")
        ans = input(str("\nY-Yes N-No->"))
        if ans == 'y' or ans == 'Y':
            receive_file(open_connection())
        elif ans == 'N' or ans == 'n':
            exit()


def receive_file(s):
    filename = s.recv(1024)
    filename = filename.decode()
    filename = os.path.basename(filename)
    filesize = s.recv(1024)
    filesize = int(filesize.decode())
    print("Do you want to download % s of size % s" % (filename, filesize))
    ans = input(str("\nY-Yes N-No->"))
    if ans == 'y' or ans == 'Y':
        ans = 'Y'
    elif ans == 'N' or ans == 'n':
        ans = 'N'
    s.send(ans.encode())
    if ans == 'Y':
        filename = "Received" + filename
        with open(filename, 'wb') as file:
            chunk_size = 1024
            chunk_file = s.recv(chunk_size)
            file.write(chunk_file)
            total_received = len(chunk_file)
            while total_received < filesize:
                chunk_file = s.recv(chunk_size)
                file.write(chunk_file)
                total_received += len(chunk_file)
                print(total_received * 100 / filesize)
        file.close()
        print("File has been recived.")
    else:
        print("!!Exiting connection!!")
        main()
    print("Do yo want to continue?")
    ans = input(str("\nY-Yes N-No->"))
    if ans == 'y' or ans == 'Y':
        ans = 'Y'
        s.send(ans.encode())
        receive_file(s)
    elif ans == 'N' or ans == 'n':
        ans = 'N'
        s.send(ans.encode())
        s.close()


def send_or_recv(s):
    ans = str(s.recv(1024).decode())
    if ans == "S":
        receive_file(s)
    elif ans == "R":
        send.choose_file(s)


def join_network():
    s = open_connection()
    send_or_recv(s)
    receive_file()
