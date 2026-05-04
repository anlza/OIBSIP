import socket
import threading

HOST = '127.0.0.1'
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive():
    while True:
        try:
            message = client.recv(1024).decode()

            if message == "NAME":
                client.send(name.encode())
            else:
                print("\n New Message:", message)

        except:
            print("Error occurred")
            client.close()
            break

def write():
    while True:
        msg = input("")
        
        
        if msg == ":)":
            msg = "😊"
        
        message = f"{name}: {msg}"
        client.send(message.encode())

name = input("Enter your name: ")

threading.Thread(target=receive).start()
threading.Thread(target=write).start()