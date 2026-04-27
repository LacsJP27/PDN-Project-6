from socket import *
import math
# Create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Bind the socket to the local IP and port 12345
serverIP = '127.0.0.1'
serverPort = 12345
serverAddress = (serverIP, serverPort);
serverSocket.bind(serverAddress)
print('The server is ready to receive')
while True:
    # Receive a byte string up to 2048 bytes long from the socket
    # The sender address is attached with the message
    messageBytes, clientAddress = serverSocket.recvfrom(2048)
    clientIP, clientPort = clientAddress
    # decode the byte string to a string object using the UTF-8 format
    message = messageBytes.decode("utf-8")
    message = message.replace(' ', '')
    strList= message.split(',')
    intList = []

    try:
        intList = [int(i) for i in strList]
        res = math.prod(intList)
        # No need for HTTP response formatting since it's not an HTTP app
        serverSocket.sendto(str(res).encode('utf-8'), clientAddress)

    except ValueError:
        serverSocket.sendto('Invalid input'.encode('utf-8'), clientAddress)
    # Send a message encoded in the UTF-8 format through the socket
