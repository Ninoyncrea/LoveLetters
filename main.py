from character import character
from action import action

if __name__ == "__main__":
    nbj = int(input("combien de joueur ?"))
    partie = character()
    dicoinfo = {}
    for i in range(0, nbj-1):
        dicoinfo["J"+str(i)] = partie.choix()
    #choisir qui commence