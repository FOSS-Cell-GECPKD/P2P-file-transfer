def send_file():
    import socket
    import os
    from requests import get
    import urllib.request
    ip=socket.gethostname()
    print("Host name:"+ip)
    def connect(host='http://google.com'):
        try:
            urllib.request.urlopen(host) 
            return True
        except:
            return False
    if connect():
        ip = get('https://api.ipify.org').text
        print("Your external ip :"+ip)
    else:
        print("No internet access")
    try:
        ip=([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] 
        if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), 
        s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, 
        socket.SOCK_DGRAM)]][0][1]]) if l][0][0])
        print("Local ip:"+ip)
    except:
      print("Not connected to any network") 

    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host=ip
    port=8080
    s.bind(('',port))
    s.listen(10)
    print("Waiting for a connection")
    conn, addr =s.accept()
    print(addr, "has connected to the system")
    filename=input(str("Please enter the filename of the file : "))
    conn.send(filename.encode())
    size = os.path.getsize(filename)
    size=str(size)
    conn.send(size.encode())
    ans = conn.recv(1024)
    ans = str(ans.decode())
    if(ans =='Y'):
        with open(filename, 'rb') as file:
            chunk_size=1024
            chunk_file=file.read(chunk_size)
            while len(chunk_file)>0:
                conn.send(chunk_file)
                chunk_file=file.read(chunk_size)
        file.close()
        print("Data has been transmitted successfully")
    else:
        print("!!Exiting!!")
    conn.close()


