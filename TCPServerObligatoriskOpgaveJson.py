from socket import *
import threading
import json

def handleClient(connectionSocket, addr):
    print(str(addr) + " has connected")
    while True:
        try:
            data = connectionSocket.recv(1024).decode()
            if not data:
                break
            request = json.loads(data)
            print("Received from client:", request)

            if "method" not in request:
                response = {"error": "Invalid request format"}
            else:
                operation = request["method"]

                if operation == "quit":
                    response = {"message": "You have disconnected"}
                    connectionSocket.send(json.dumps(response).encode())
                    break

                if "Tal1" not in request or "Tal2" not in request:
                    response = {"error": "Invalid request format"}
                else:
                    num1 = int(request["Tal1"])
                    num2 = int(request["Tal2"])

                    if operation == "Random":
                        import random
                        result = random.randint(num1, num2)
                    elif operation == "Add":
                        result = num1 + num2
                    elif operation == "Subtract":
                        result = num1 - num2
                    else:
                        response = {"error": "Unknown operation"}
                        connectionSocket.send(json.dumps(response).encode())
                        continue

                    response = {"result": result}

                print("Sending response to client:", response)
                connectionSocket.send(json.dumps(response).encode())
        except ValueError:
            response = {"error": "Invalid JSON format"}
            connectionSocket.send(json.dumps(response).encode())

    print(str(addr) + " has disconnected")
    connectionSocket.close()

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('Server is ready to listen')

while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=handleClient, args=(connectionSocket, addr)).start()
