from game import Game
from interface import Interface
if __name__ == "__main__":
    """    nbj = int(input("combien de joueur ?"))
    """
    inter = Interface()
    nbj = inter.ask_players()
    game = Game(nbj)
    game.initialisation()
    game.start()
