import socket

def main():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	addr = ("0.0.0.0", 17891)
	sock.bind(addr)
	sock.listen(5)
	while True:
		(connectedSock, clientAddress) = sock.accept()
	
		try:
			msg = sock.recv(1024).decode()
			msg = "Length of " + msg + ": " + len(msg)
			sock.sendall(msg.encode())

		except ConnectionAbortedError:
			sock.close()
		
