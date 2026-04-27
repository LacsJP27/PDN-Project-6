from socket import *
import math
# Create a TCP welcoming socket
welcomeSocket = socket(AF_INET, SOCK_STREAM)
# Bind it to the local IP and port 12345
serverIP = '127.0.0.1'
serverPort = 12000
serverAddress = (serverIP, serverPort)
welcomeSocket.bind(serverAddress)
# Welcome socket begins listening for incoming TCP requests
# Allows up to 1 pending requests for connection in the queue
welcomeSocket.listen(1)
print('The server is ready to receive')
while True:
    # server waits on accept() for incoming requests
    # a new connection socket is created on return
    connectionSocket, clientAddress = welcomeSocket.accept()
    clientIP, clientPort = clientAddress
    # receive a byte string from the connection socket
    messageBytes = connectionSocket.recv(1024)
    message = messageBytes.decode("utf-8")
    print(f'message from {clientIP}:{clientPort} = {message}')
    message = message.replace(' ', '')
    strList= message.split(',')
    intList = []

    try:
        intList = [int(i) for i in strList]
        res = math.prod(intList)
        # No need for HTTP response formatting since it's not an HTTP app
        connectionSocket.send(str(res).encode('utf-8'))

    except ValueError:
        connectionSocket.send('Invalid input'.encode('utf-8'))
        


    # send a byte string to the connection socket
    # close the connection socket to this client
    connectionSocket.close()
    # the welcoming socket is still open for new clients
