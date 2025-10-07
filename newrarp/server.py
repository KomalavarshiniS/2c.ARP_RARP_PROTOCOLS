import socket
s = socket.socket()
s.connect(('localhost', 9000))

while True:
    ip = input("Enter MAC Address : ")
    if ip.lower() in ["exit", "quit"]:
        break
    s.send(ip.encode())
    print("Logical Address:", s.recv(1024).decode())

s.close()
