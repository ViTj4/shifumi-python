import socket
import random
import threading


# Fonction qui gère une partie du jeu
def play_game(conn, addr):
    # Demande le nom du client
    conn.send("Quel est votre nom ?\n".encode())
    name = conn.recv(1024).decode().strip()

    # Demande au client de choisir une option
    conn.send("Choisissez une option : Pierre, Papier, ou Ciseau ?\n".encode())
    client_choice = conn.recv(1024).decode().strip()

    # Détermine le choix du serveur au hasard
    options = ['Pierre', 'Papier', 'Ciseau']
    server_choice = random.choice(options)

    # Détermine le résultat de la partie
    if client_choice == server_choice:
        result = "Égalité !"
    elif client_choice == "Pierre" and server_choice == "Ciseau" \
            or client_choice == "Papier" and server_choice == "Pierre" \
            or client_choice == "Ciseau" and server_choice == "Papier":
        result = f"{name} a gagné !"
    else:
        result = "Le serveur a gagné !"

    # Envoie le résultat de la partie au client
    conn.send(result.encode())

    # Ferme la connexion
    conn.close()
    print(f"Connexion avec {addr} terminée.")


# Programme principal
HOST = 'localhost'
PORT = 5000

# Crée un objet socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind l'objet socket avec l'adresse et le port
server_socket.bind((HOST, PORT))

# Écoute les connexions entrantes
server_socket.listen()

print(f"Le serveur écoute sur le port {PORT}...")

while True:
    # Attend une connexion entrante
    conn, addr = server_socket.accept()
    print(f"Nouvelle connexion avec {addr}")

    # Crée un thread pour gérer la partie
    t = threading.Thread(target=play_game, args=(conn, addr))
    t.start()
