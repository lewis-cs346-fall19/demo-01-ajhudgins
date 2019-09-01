import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ("0.0.0.0", 17900)
sock.bind(addr)
sock.listen(5)

while True:
	(conn, addr) = sock.accept()
	print("Connected")
			
	conn.sendall("Hello, this is the server")
	
	for i in range(0,99): 
		clientmsg = conn.recv(1024).decode()
		print(clientmsg)

		conn.sendall(clientmsg[0:14] + ", back at ya * " + str(i * i))
  
	conn.close()

