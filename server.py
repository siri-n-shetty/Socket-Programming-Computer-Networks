import socket
import ssl

def perform_operation(operation, data):
    if operation == 1:
        return data[::-1]
    elif operation == 2:
        return data.upper()
    elif operation == 3:
        return data.lower()
    elif operation == 4:
        names = data.split()
        initials = ''.join([name[0].upper() for name in names])
        return initials
    else:
        return "Invalid operation"

def main():
    host = '127.0.0.1'
    port = 12000

    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile='cert.pem', keyfile='private_key.pem')  # Adjust file paths as necessary

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(5)
        print(f"Server listening on {host}:{port}")

        while True:
            client_socket, addr = server_socket.accept()
            with context.wrap_socket(client_socket, server_side=True) as secure_socket:
                print('Got connection from', addr)

                data = secure_socket.recv(1024).decode()
                print("Received from the client:", data)

                operation_choice = int(secure_socket.recv(1024).decode())
                print("Operation choice from the client:", operation_choice)

                result = perform_operation(operation_choice, data)

                secure_socket.sendall(result.encode())

if __name__ == '__main__':
    main()
