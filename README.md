# 2c.SIMULATING ARP /RARP PROTOCOLS
## AIM
To write a python program for simulating ARP protocols using TCP.
## ALGORITHM:
## Client:
1. Start the program
2. Using socket connection is established between client and server.
3. Get the IP address to be converted into MAC address.
4. Send this IP address to server.
5. Server returns the MAC address to client.
## Server:
1. Start the program
2. Accept the socket which is created by the client.
3. Server maintains the table in which IP and corresponding MAC addresses are
stored.
4. Read the IP address which is send by the client.
5. Map the IP address with its MAC address and return the MAC address to client.
P
## PROGRAM - ARP
### Client.py
```
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

```
### Server.py
```
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

```
## OUPUT - ARP
### Client.py
![alt text](<Screenshot 2025-10-07 090355.png>)
### Server.py
![alt text](<Screenshot 2025-10-07 090402.png>)

## PROGRAM - RARP
### Client.py
```
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

```
### Server.py
```
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
```

## OUPUT -RARP
### Client.py
![alt text](<Screenshot 2025-10-07 091059.png>)
### Server.py
![alt text](<Screenshot 2025-10-07 091106.png>)
## RESULT
Thus, the python program for simulating ARP protocols using TCP was successfully 
executed.
