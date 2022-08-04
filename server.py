import socket
import base64

def recvall(sock):
	BUFF_SIZE = 4096
	data = b''
	while True:
		part = sock.recv(BUFF_SIZE)
		data += part
		if len(part) < BUFF_SIZE:
			break
	return data 

PORT=7878
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('0.0.0.0', PORT))
s.listen(1)
while True:
	try:
		c, addr = s.accept()
		data = recvall(c)
		data = data.strip().decode()
		data = data.split()
		msg = "".join([i[2:] for i in data])
		msg = bytes.fromhex(msg).decode()
		msg = msg.split()
		msg = "".join([chr(int(i)) for i in msg])
		msg = msg + "=="
		msg = msg.encode()
		msg = base64.b64decode(msg).decode()
		msg = f"Your decoded message is : {msg}"
		c.send(msg.encode())
	except Exception as e:
		print(e)
	finally:
		c.close()
