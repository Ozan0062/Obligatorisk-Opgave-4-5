from socket import *
import threading

def handleClient(connectionSocket, addr):
    print(str(addr) + " has connected")
    while True:
        sentence = connectionSocket.recv(1024).decode()
        print("Received from client: " + sentence)

        if sentence == "quit":
           print(str(addr)+" has disconnected")
           break

        # Parse the client's request
        parts = sentence.split(';')
        if len(parts) != 3:
            response = "Invalid request format"
        else:
            operation = parts[0]
            num1 = int(parts[1])
            num2 = int(parts[2])

            if operation == "Random":
                import random
                result = random.randint(num1, num2)
            elif operation == "Add":
                result = num1 + num2
            elif operation == "Subtract":
                result = num1 - num2
            else:
                response = "Unknown operation"
                connectionSocket.send(response.encode())
                continue  # Continue to the next iteration of the loop

            response = str(result)

        print("Sending response to client: " + response)
        connectionSocket.send(response.encode())

    connectionSocket.close()

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('Server is ready to listen')

while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=handleClient, args=(connectionSocket, addr)).start()
