import socket 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ("0.0.0.0", 17900)
sock.connect(addr)

servermsg = sock.recv(1024).decode()
print(servermsg)

for i in range(0,99):
	sock.sendall("You're awesome * " + str(i))
	
	try:
		servermsg = sock.recv(1024).decode()
		print(servermsg)
	except:
		sock.close()
sock.close()

