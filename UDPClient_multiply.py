from socket import *
# Create a UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
# Binding a socket is optional on the client side

message = input("Enter numbers to multiply in this format [1, 2, 3] : ")

messageBytes = message.encode("utf-8")
# Send a message through the client socket
# The destination is specified by a tuple of IP and port
serverIP = '127.0.0.1'
serverPort = 12345
serverAddress = (serverIP, serverPort);
clientSocket.sendto(messageBytes, serverAddress)
# Receive a byte string up to 2048 bytes long from the client socket
# The sender information is attached with the message
modifiedMessageBytes, serverAddress = clientSocket.recvfrom(2048)
modifiedMessage = modifiedMessageBytes.decode("utf-8")
serverIP, serverPort = serverAddress
print(f'message from {serverIP}:{serverPort} = {modifiedMessage}')
# then loop back up and ask for a message again
clientSocket.close()
