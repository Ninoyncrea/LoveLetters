from game import Game
from interface import Interface
from fenetre import Fenetre
if __name__ == "__main__":
    noms_joueurs = {"Joueur1": "Nom1", "Joueur2": "Nom2", "Joueur3": "Nom3"}
    fenet = Fenetre
    interface = Interface()
    nbj = interface.ask_players()
    fenet.afficher_boutons_joueurs(noms_joueurs)
    game = Game(nbj)
    game.initialisation()
    game.start()
