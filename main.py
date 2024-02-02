from game import Game
from interface import Interface
from fenetre import Fenetre
from serveur import ChatServer
if __name__ == "__main__":
    """server = ChatServer("localhost", 1900)
    server.start_server()"""
    noms_joueurs = {"Joueur1": "Nom1", "Joueur2": "Nom2", "Joueur3": "Nom3"}
    interface = Interface()
    nbj = interface.ask_players()
    game = Game(nbj)
    game.initialisation()
    game.start()
