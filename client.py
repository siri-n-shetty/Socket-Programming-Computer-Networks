import socket
import ssl

def get_user_input():
    print("Select operation:")
    print("1) Reverse the string")
    print("2) Capitalize the entire string")
    print("3) Decapitalize the entire string")
    print("4) Display initials of the person (assuming the string is a name)")
    choice = input("Enter your choice (1-4): ")
    return int(choice)

def main():
    host = '127.0.0.1'
    port = 12000

    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE  # Only for self-signed certs

    with socket.create_connection((host, port)) as sock:
        with context.wrap_socket(sock, server_hostname=host) as secure_socket:
            message_to_send = input("Enter a string: ")
            secure_socket.sendall(message_to_send.encode())
            print(f"Sent to server: {message_to_send}")

            operation_choice = get_user_input()
            secure_socket.sendall(str(operation_choice).encode())

            result = secure_socket.recv(1024).decode()
            print(f"Result from server: {result}")

if __name__ == '__main__':
    main()
