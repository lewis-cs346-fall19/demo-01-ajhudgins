def main():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	addr = ("0.0.0.0", 17891)
	sock.bind(addr)
	sock.listen(5)
	while(true):
		(connectedSock, clientAddress) = sock.accept()

