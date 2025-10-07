import socket
s = socket.socket()
s.bind(('localhost', 9000))
s.listen(5)
print("Server listening on port 9000...")

c, addr = s.accept()
print("Connected with", addr)

address = {
    "6A:08:AA:C2": "192.168.1.100",
    "8A:BC:E3:FA": "192.168.1.99"
}

while True:
    mac = c.recv(1024).decode()
    if not mac:
        break
    print("Client requested:", mac)
    ip = address.get(mac, "Not Found")
    c.send(ip.encode())

c.close()
s.close()
