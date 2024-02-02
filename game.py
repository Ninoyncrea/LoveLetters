from action import Action
from character import Character
from interface import Interface
from fenetre import Fenetre


class Game:
    def __init__(self, nbjoueur):
        self.nbjoueur = nbjoueur
        self.dicoinfo = {}
        self.partie = Character()
        self.act = Action
        self.dictmort = {"admin": "admin"}
        self.dicoactu = None
        self.mort = None

    def initialisation(self):
        for i in range(self.nbjoueur):
            self.dicoinfo["J" + str(i)] = self.partie.choix(self.dicoinfo)

    def start(self):
        dicoinfoini = self.dicoinfo.copy()

        while len(self.dicoinfo) > 1:
            for nom, role in dicoinfoini.items():
                fenet = Fenetre()
                self.dictmort = self.act(self.dicoinfo, role, nom, self.partie, self.dictmort).getdicomort()
                if list(self.dictmort.values())[-1] != "admin":
                    self.mort = list(self.dictmort.values())[-1]
                fenet.afficher_boutons_joueurs(self.dicoinfo, self.dictmort)
                print(self.dicoinfo)
                print(nom)
                print(role)

                if nom in list(self.dicoinfo.keys()):

                    pioche = self.partie.choix(self.dicoinfo)
                    # demander quel carte piocher
                    inter = Interface()
                    inter.run(nom, pioche, self.dicoinfo)
                    carte = inter.getchoix()
                    if carte == pioche:
                        ACT = self.act(self.dicoinfo, pioche, nom, self.partie, self.dictmort)
                        self.dicoinfo, self.dicoactu = ACT.action1()
                    if carte == role:
                        self.dicoinfo[nom] = pioche
                        ACT = self.act(self.dicoinfo, role, nom, self.partie, self.dictmort)
                        self.dicoinfo, self.dicoactu = ACT.action1()

                    self.dictmort.update(self.dicoactu)
                    print(self.dictmort)

        print("fin de partie")
        if len(self.dicoinfo) == 1:
            print("trop fort " + str(self.dicoinfo.keys) + " a gagné la partie")
        if len(self.dicoinfo) == 0:
            print("mentalité de perdant")

    def getdicoinfo(self):
        return self.dicoinfo
