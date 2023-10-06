import socket
import threading
import json
import random
def handle_client(client_socket):
    try:
        data = client_socket.recv(1024).decode('utf-8')
        
        if not data:
            return
        request = json.loads(data)
        
        if 'function' not in request or 'num1' not in request or 'num2' not in request:
            response = {"error": "Invalid request format. Please send: {'function': 'Add', 'num1': 5, 'num2': 3}"}
        else:
            function = request['function']
            num1 = request['num1']
            num2 = request['num2']
            
            if function == "Add":
                result = num1 + num2
            elif function == "Subtract":
                result = num1 - num2
            elif function == "Random":
                result = random.randint(num1, num2)
            else:
                result = {"error": "Unknown function. Valid functions are: Add, Subtract, Random"}
            
            response = {"result": result}
        
        client_socket.send(json.dumps(response).encode('utf-8'))
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        client_socket.close()
host = '0.0.0.0'
port = 215

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)
print(f"Server listening on {host}:{port}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address[0]}:{client_address[1]}")
    
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()