import socket

s = socket.socket()

PORT = 7878

s.connect(("127.0.0.1", PORT))
inp = input("input>")
s.send(inp.encode())
print(s.recv(4096))
s.close()