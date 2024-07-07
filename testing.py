
import socket

def start_server():
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.bind(('localhost', 12345))
	server_socket.listen()
	print("Server is listening on localhost:12345")
	
	while True:
		client_socket, addr = server_socket.accept()
		print(f"Connection from {addr} has been established.")
		client_socket.send(bytes("Welcome to the server!", "utf-8"))
		client_socket.close()

if __name__ == "__main__":
	connect_to_server()