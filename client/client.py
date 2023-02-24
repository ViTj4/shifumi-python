import socket

# Établit la connexion avec le serveur
HOST = 'localhost'
PORT = 5000
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Récupère le nom du client
name = input("Quel est votre nom ?\n")
client_socket.send(name.encode())

# Récupère le choix de l'utilisateur
choice = input("Choisissez une option : Pierre, Papier, ou Ciseau ?\n")
client_socket.send(choice.encode())

# Récupère le résultat de la partie
result = client_socket.recv(1024).decode().strip()
print(result)

# Ferme la connexion
client_socket.close()