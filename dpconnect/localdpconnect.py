import socket
import threading

def start_listener():
    host = '0.0.0.0'  # Listen on all available interfaces
    port = 4444

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)

    print(f"[*] Listening on {host}:{port}")

    while True:
        client_socket, addr = server.accept()
        print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")

        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

def handle_client(client_socket):
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(data.decode("utf-8"))
            
            # Example: Send a command back to the client
            command = input("Shell> ")
            client_socket.send(command.encode("utf-8"))
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

def main():
    start_listener()

if __name__ == "__main__":
    main()
