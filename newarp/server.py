import socket

s = socket.socket()
s.connect(('localhost', 8000))

while True:
    ip = input("Enter logical Address (IP) : ")
    if ip.lower() in ["exit", "quit"]:
        break
    s.send(ip.encode())
    mac = s.recv(1024).decode()
    print("MAC Address:", mac)

s.close()
