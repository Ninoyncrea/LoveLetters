from action import Action
from character import Character


class Game:
    def __init__(self, nbjoueur):
        self.nbjoueur = nbjoueur
        self.dicoinfo = {}
        self.partie = Character()
        self.act = Action

    def initialisation(self):
        for i in range(self.nbjoueur):
            self.dicoinfo["J" + str(i)] = self.partie.choix()

    def start(self):
        dicoinfoini = self.dicoinfo.copy()

        while len(self.dicoinfo) > 1:
            for nom, role in dicoinfoini.items():
                print(self.dicoinfo)
                print(nom)
                print(role)
                if nom not in list(self.dicoinfo.keys()):
                    continue

                pioche = self.partie.choix()
                # demander quel carte piocher
                carte = role
                if carte == pioche:
                    self.dicoinfo = self.act(self.dicoinfo, pioche, nom, self.partie).action1()
                if carte == role:
                    self.dicoinfo[nom] = pioche
                    self.dicoinfo = self.act(self.dicoinfo, role, nom, self.partie).action1()
                if self.partie.getnbrole() <= 0:
                    print("fin de partie")
                    print(self.dicoinfo)
                    exit()
        print("fin de partie")
