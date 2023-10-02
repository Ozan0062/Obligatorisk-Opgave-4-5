from socket import *
import json

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
        request = {"method": "quit"}
        clientSocket.send(json.dumps(request).encode())

        # Wait for the server's response
        response = clientSocket.recv(1024).decode()
        response_data = json.loads(response)

        if "message" in response_data:
            print('Server response:', response_data["message"])
        else:
            print('Server response:', response_data)  # Handle other responses here if needed

        break

    num1 = input('Enter first number: ')
    num2 = input('Enter second number: ')

    request = {"method": operation, "Tal1": int(num1), "Tal2": int(num2)}
    clientSocket.send(json.dumps(request).encode())

    response = clientSocket.recv(1024).decode()
    response_data = json.loads(response)
    if "error" in response_data:
        print('Server response: Error -', response_data["error"])
    else:
        print('Server response:', response_data["result"])

clientSocket.close()
