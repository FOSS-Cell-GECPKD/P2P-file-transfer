import os
import socket
import send
from peer import main


def open_connection():  # connecting to the host
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = input(str("Enter the host address of the sender : "))
        port = 8080
        s.connect((host, port))
        print(" Connected to the host... ")
        return s
    except:  # port busy error
        print("Connection error do you want to try again?")
        ans = input(str("\nY-Yes N-No->"))
        if ans == 'y' or ans == 'Y':
            return open_connection()  # Trying again to check whether port is free
        elif ans == 'N' or ans == 'n':
            exit()


def receive_file(s):  # Receive file from other peer
    file_name = s.recv(1024)
    file_name = file_name.decode()
    file_name = os.path.basename(file_name)
    file_size = s.recv(1024)
    file_size = int(file_size.decode())
    print("Do you want to download % s of size % s" % (file_name, file_size))
    ans = input(str("\nY-Yes N-No->"))
    if ans == 'y' or ans == 'Y':
        ans = 'Y'
    elif ans == 'N' or ans == 'n':
        ans = 'N'
    s.send(ans.encode())
    if ans == 'Y':  # Create and write into the file
        with open(file_name, 'wb') as file:
            chunk_size = 1024
            chunk_file = s.recv(chunk_size)
            file.write(chunk_file)
            total_received = len(chunk_file)
            while total_received < file_size:
                chunk_file = s.recv(chunk_size)
                file.write(chunk_file)
                total_received += len(chunk_file)
                print(total_received * 100 / file_size)
        file.close()
        print("File has been received.")
    else:
        print("!!Exiting connection!!")
        s.close()  # Ending Connection
        main()  # Going back to the beginning and start again
    print("Do yo want to continue?")  # Ask to know whether continue or end the file Transfer
    ans = input(str("\nY-Yes N-No->"))
    if ans == 'y' or ans == 'Y':
        ans = 'Y'
        s.send(ans.encode())
        receive_file(s)
    elif ans == 'N' or ans == 'n':
        ans = 'N'
        s.send(ans.encode())
        s.close()


def send_or_recv(s):  # Getting know whether this peer should send or receive file
    ans = str(s.recv(1024).decode())
    if ans == "S":
        receive_file(s)
    elif ans == "R":
        send.choose_file(s)


def join_network():  # Join the network created by create_network()
    s = open_connection()
    send_or_recv(s)