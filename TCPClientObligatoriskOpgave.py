from socket import *

serverName = "localhost"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

while True:
    while True:
        operation = input('Enter operation (Random/Add/Subtract): ')
        
        if operation.lower() in ('random', 'add', 'subtract', 'quit'):
            break
        else:
            print('Invalid operation. Please enter a valid operation.')

    if operation.lower() == 'quit':
        clientSocket.send('quit'.encode())
        break

    num1 = input('Enter first number: ')
    num2 = input('Enter second number: ')

    request = f"{operation};{num1};{num2}"
    clientSocket.send(request.encode())

    response = clientSocket.recv(1024).decode()
    print('Server response: ', response)

clientSocket.close()
