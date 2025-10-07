import socket

s = socket.socket()
s.bind(('localhost', 8000))
s.listen(5)
print("Server is listening on port 8000...")

c, addr = s.accept()
print("Connected with", addr)

address = {
    "165.165.80.80": "6A:08:AA:C2",
    "165.165.79.1": "8A:BC:E3:FA"
}

while True:
    ip = c.recv(1024).decode()
    if not ip:
        break
    print("Client requested:", ip)
    mac = address.get(ip, "Not Found")
    c.send(mac.encode())

c.close()
s.close()
