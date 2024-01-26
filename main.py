from game import Game
from interface import Interface
from fenetre import Fenetre
if __name__ == "__main__":
    noms_joueurs = {"Joueur1": "Nom1", "Joueur2": "Nom2", "Joueur3": "Nom3"}
    interface = Interface()
    nbj = interface.ask_players()
    game = Game(nbj)
    game.initialisation()
    game.start()
