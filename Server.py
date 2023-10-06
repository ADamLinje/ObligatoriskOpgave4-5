import socket
import threading
import random
def handle_client(client_socket):
    try:
        data = client_socket.recv(1024).decode('utf-8')
        
        if not data:
            return
        parts = data.strip().split()
        
        if len(parts) != 3:
            response = "Invalid request format. Please send: <Function>; <Number1>; <Number2>"
        else:
            function, num1, num2 = parts
            
            if function == "Add":
                result = int(num1) + int(num2)
            elif function == "Subtract":
                result = int(num1) - int(num2)
            elif function == "Random":
                result = random.randint(int(num1), int(num2))
            else:
                result = "Unknown function. Valid functions are: Add, Subtract, Random"
            
            response = str(result)
        
        client_socket.send(response.encode('utf-8'))
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        client_socket.close()

host = '0.0.0.0'
port = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)
print(f"Server listening on {host}:{port}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address[0]}:{client_address[1]}")
    
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()
      