import socket 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ("0.0.0.0", 17897)
sock.connect(addr)
servermsg = sock.recv(1024)

print(servermsg)

sock.sendall("Hello, this is the client")

sock.close()

