import socket
from _thread import *
import os
import recive


def get_ip():  # Used to get the ip address and host name for creating a network to connect
    ip = socket.gethostname()
    print("Host name:" + ip)

    try:
        ip = ([l for l in (
            [ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [
                [(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in
                 [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0])
        print("Local ip:" + ip)
    except:
        print("Not connected to any network")


def end_connection(conn):  # Ending connection

    print("Disconnected ")
    conn.close()

    print("Connect to another")
    ans = input(str("\nY-Yes N-No->"))
    if ans == 'y' or ans == 'Y':
        socket_connection()
    elif ans == 'N' or ans == 'n':
        print("Exiting server")
        exit()


def choose_file(conn):  # Selecting file to send
    filename = input(str("Please enter the path of the file : "))
    try:  # connection error while communication
        conn.send(filename.encode())
        try:  # file doesn't exists
            file_size = os.path.getsize(filename)
        except:
            print("Unable to find file try again")
            choose_file(conn)
        file_size = str(file_size)
        conn.send(file_size.encode())
        ans = conn.recv(1024)
        ans = str(ans.decode())
        if ans == 'N':
            print("Ending connection")
            end_connection(conn)
        if ans == 'Y':
            with open(filename, 'rb') as file:
                chunk_size = 1024
                chunk_file = file.read(chunk_size)
                while len(chunk_file) > 0:
                    conn.send(chunk_file)
                    chunk_file = file.read(chunk_size)
            file.close()
            print("Data has been transmitted successfully")
            ans = conn.recv(1024)
            ans = str(ans.decode())
            if ans == "Y" or ans == "y":
                choose_file(conn)
            else:
                print("!!Exiting!!")
                end_connection()
    except:
        print("!!Error!!\nDo you want to try again?")
        ans = input(str("\nY-Yes N-No->"))
        if ans == 'y' or ans == 'Y':
            print("Try reconnecting")
            socket_connection()
        elif ans == 'N' or ans == 'n':
            print("Closing connection")
            end_connection()


def send_or_receive(conn):  # Both peers can send and receive file
    choice = input("""
                    S: Send a file
                    R: Receive a file
                    Please enter your choice (S/R):""")
    if choice == "S" or choice == "s":
        conn.send("S".encode())
        choose_file(conn)
    elif choice == "R" or choice == "r":
        conn.send("R".encode())
        recive.file(conn)
    else:
        print("You must only select either S or R")
        print("please try again")


def socket_connection():  # Creating the socket connection
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port = 8080
        s.bind(('', port))

        s.listen(10)
        print("Waiting for a connection")
        conn, addr = s.accept()

        print(addr, "has connected to the system")

        send_or_receive(conn)
    except:
        print("Connection error")
        print("Do you want to try again?")
        ans = input(str("\nY-Yes N-No->"))
        if ans == 'y' or ans == 'Y':
            socket_connection()
        elif ans == 'N' or ans == 'n':
            print("Exiting server")
            exit()


def create_network():  # Getting ip and creating socket connection
    get_ip()
    socket_connection()
