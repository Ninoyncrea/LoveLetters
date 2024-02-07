import socket
import threading
import pickle
import time
from src.game import Game

class Server:
    def __init__(self, host, port):
        self.HOST = host
        self.PORT = port
        self.clients = {}
        self.G1 = Game(4)
        self.G1.initialisation()
        self.dico = self.G1.getdicoinfo()
        self.pioche = self.G1.choix()
        self.button_backgrounds = [
            [self.dico["0"] + ".jpg", "facecache.jpg", "facecache.jpg", "facecache.jpg"],
            ["facecache.jpg", self.dico["1"] + ".jpg", "facecache.jpg", "facecache.jpg"],
            ["facecache.jpg", "facecache.jpg", self.dico["2"] + ".jpg", "facecache.jpg"],
            ["facecache.jpg", "facecache.jpg", "facecache.jpg", self.dico["3"] + ".jpg"]
        ]
        self.current_button_owner = 0
        self.button_pioche = [
            [self.pioche + ".jpg", "taverneV2.jpg", "taverneV2.jpg", "taverneV2.jpg"],
            ["facecache.jpg", "taverneV2.jpg", "taverneV2.jpg", "taverneV2.jpg"],
            ["facecache.jpg", "taverneV2.jpg", "taverneV2.jpg", "taverneV2.jpg"],
            ["facecache.jpg", "taverneV2.jpg", "taverneV2.jpg", "taverneV2.jpg"]
        ]
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.update_thread = threading.Thread(target=self.send_updated_data)
        self.listemort = []
    def start(self):
        self.server_socket.bind((self.HOST, self.PORT))
        self.server_socket.listen()
        print("Attente des connexions des clients...")
        self.update_thread.start()
        try:
            while True:
                conn, addr = self.server_socket.accept()
                thread = threading.Thread(target=self.handle_client, args=(conn, addr))
                thread.start()
        except KeyboardInterrupt:
            print("Arrêt du serveur...")
        finally:
            for client in self.clients.keys():
                client.close()
            self.server_socket.close()

    def handle_client(self, conn, addr):
        print(f"Nouveau client connecté: {addr}")
        client_id = self.assign_client_id(conn)
        self.clients[conn] = client_id

        try:
            while True:
                data = conn.recv(4096)
                if not data:
                    break
                action = data.decode()
                self.handle_action(action)
        except Exception as e:
            print(f"Erreur lors de la communication avec le client {addr}: {e}")
        finally:
            del self.clients[conn]
            conn.close()
            print(f"Connexion avec le client {addr} fermée")

    def assign_client_id(self, conn):
        client_id = len(self.clients)
        return client_id

    def send_updated_data(self):
        while True:
            for conn, client_id in self.clients.items():
                data = pickle.dumps((self.button_backgrounds[client_id], self.button_pioche[client_id], client_id))
                conn.sendall(data)
            time.sleep(1)

    def handle_action(self, action):
        joueur = int(action[0])
        rolejoue = str(action[1:])
        self.dico = self.G1.getdicoinfo()
        self.listemort = self.G1.getlistemort()
        if rolejoue == self.dico[str(joueur)]:
            print(self.pioche)
            self.G1.changemainetpioche(joueur, rolejoue, self.pioche)
        if rolejoue == "princesse" or rolejoue == "comtesse" or rolejoue == "servante":
            self.dico, self.listemort = self.G1.jouer(joueur, rolejoue)
        listeaction = rolejoue.split()
        if len(listeaction) == 2:
            if listeaction[0] == "pretre" or listeaction[0] == "prince" or listeaction[0] == "Baron" or listeaction[0] == "roi":
                self.dico, self.listemort = self.G1.jouer(joueur, listeaction[0], str(listeaction[1]))
        if len(listeaction) == 3:
            if listeaction[0] == "garde":
                self.dico, self.listemort = self.G1.jouer(joueur, listeaction[0], str(listeaction[1]), listeaction[2])
        if len(self.dico) ==1:
            print(self.dico.keys()+" a gagné la partie")
        self.setbutton_backgrounds(self.dico)
        joueur += 1
        print("ioe")
        while str(joueur) in self.listemort:
            print("iojiefz")
            joueur += 1
            if joueur > 3:
                joueur = 0
        role = self.G1.choix()
        self.setbutton_pioche(joueur, role)
        print(self.listemort)

    def setbutton_backgrounds(self, dico):
        rico = dico
        listemortV = []
        for i in range(4):
            if str(i) not in list(rico.keys()):
                rico[str(i)] = "die"
                listemortV.append(i)
        self.button_backgrounds = [
            [rico["0"] + ".jpg", "facecache.jpg", "facecache.jpg", "facecache.jpg"],
            ["facecache.jpg", rico["1"] + ".jpg", "facecache.jpg", "facecache.jpg"],
            ["facecache.jpg", "facecache.jpg", rico["2"] + ".jpg", "facecache.jpg"],
            ["facecache.jpg", "facecache.jpg", "facecache.jpg", rico["3"] + ".jpg"]
        ]
        if len(listemortV)>0:
            for elt in listemortV:
                for i in range(len(self.button_backgrounds[elt])):
                    self.button_backgrounds[i][elt] = "die.jpg"
        print(self.button_backgrounds)
    def setbutton_pioche(self, joueur, role):
        self.button_pioche = [
            ["taverneV2.jpg", "taverneV2.jpg", "taverneV2.jpg", "taverneV2.jpg"],
            ["taverneV2.jpg", "taverneV2.jpg", "taverneV2.jpg", "taverneV2.jpg"],
            ["taverneV2.jpg", "taverneV2.jpg", "taverneV2.jpg", "taverneV2.jpg"],
            ["taverneV2.jpg", "taverneV2.jpg", "taverneV2.jpg", "taverneV2.jpg"]]
        for i in range(0, 4):
            if joueur == i:
                self.button_pioche[i][joueur] = role + ".jpg"
            if joueur != i:
                self.button_pioche[i][joueur] = "facecache.jpg"
# Exemple d'utilisation
"""if __name__ == "__main__":
    server = Server('127.0.0.1', 5555)
    server.start()
"""