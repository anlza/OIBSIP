import socket
import threading

HOST = '127.0.0.1'
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
names = []

print("Server started...")

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)

            # 💾 Save message history
            with open("chat_history.txt", "a") as f:
                f.write(message.decode() + "\n")

        except:
            index = clients.index(client)
            clients.remove(client)
            name = names[index]
            broadcast(f"{name} left the chat.".encode())
            names.remove(name)
            client.close()
            break

def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {address}")

        client.send("NAME".encode())
        name = client.recv(1024).decode()

        names.append(name)
        clients.append(client)

        print(f"{name} joined the chat")
        broadcast(f"{name} joined the chat!".encode())

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()