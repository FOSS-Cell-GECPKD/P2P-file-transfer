import os
import socket
import send
from peer import main


def write_file(s, file_name, file_size):  # Writes into the file
    with open(file_name, 'wb') as file:
        chunk_size = 1024
        chunk_file = s.recv(chunk_size)
        file.write(chunk_file)
        total_received = len(chunk_file)
        while total_received < file_size:
            chunk_file = s.recv(chunk_size)
            file.write(chunk_file)
            total_received += len(chunk_file)
    file.close()
    print("File has been received.")


def open_connection():  # connecting to the host
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = input(str("Enter the host address of the sender : "))
        port = 8080
        s.connect((host, port))
        print(" Connected to the host... ")
        return s
    except:
        print("Port busy try again later")


def receive_file(s):  # Receive file from other peer
    file_name = os.path.basename(s.recv(1024).decode())
    file_size = int(s.recv(1024).decode())
    print("Do you want to download % s of size % s" % (file_name, file_size))
    ans = input(str("\nY-Yes N-No->"))
    if ans == 'y' or ans == 'Y':
        s.send('Y'.encode())
        write_file(s, file_name, file_size)
    elif ans == 'N' or ans == 'n':
        s.send('N'.encode())
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
