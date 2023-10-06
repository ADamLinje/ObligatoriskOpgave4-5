import socket
import json

server_address = ('localhost', 215)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect(server_address)

    function = input("Enter function (Add, Subtract, Random): ")
    num1 = int(input("Enter number1: "))
    num2 = int(input("Enter number2: "))

    request = {"function": function, "num1": num1, "num2": num2}

    data = json.dumps(request)
    client_socket.send(data.encode('utf-8'))

    response = client_socket.recv(1024).decode('utf-8')
    response = json.loads(response)
    print(f"Server response: {response}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    client_socket.close()