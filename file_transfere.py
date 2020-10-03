def send_file():
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
    print("Data has been transmitted successfully")

def receive_file():
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
    print("File has been recived.")

def menu():
    choice=input("""
                S: Send a file
                R: Receive a file
                Please enter your choice (S/R):""")
    if choice=="S" or choice=="s":
        send_file()
    elif choice=="R" or choice=="r":
        receive_file()
    else:
        print("You must only select either S or R")
        print("please try again")
        menu()

def main():
    menu()
    ans=input("Do you want to continue [y/n]? ")
    if ans=="Y" or ans=="y":
        main()

main()
