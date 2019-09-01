import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ("0.0.0.0", 17897)
sock.bind(addr)
sock.listen(5)

while True:
	(conn, addr) = sock.accept()
	print("Connected")
	

	conn.sendall("Hello, this is the server")
	clientmsg = conn.recv(1024)
	print(clientmsg)

	conn.close()

