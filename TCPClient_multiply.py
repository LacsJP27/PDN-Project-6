from socket import *
# Create a TCP socket
clientSocket = socket(AF_INET, SOCK_STREAM)
# Connect to a server process using a tuple of IP and port
serverIP = '127.0.0.1'
serverPort = 12000
serverAddress = (serverIP, serverPort)
clientSocket.connect(serverAddress)
# Send a byte string to the client socket
message = input("Enter numbers to multiply in this format [1, 2, 3] : ")
clientSocket.send(message.encode("utf-8"))
# Receive a byte string from the client socket
modifiedMessageBytes = clientSocket.recv(1024)
print('From Server: ', modifiedMessageBytes.decode("utf-8"))
clientSocket.close()
