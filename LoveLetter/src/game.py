import random as rd


class Game:
    def __init__(self, nbjoueur):
        self.nbjoueur = nbjoueur
        self.role = None
        self.dicoinfo = {}
        self.dictmort = {"admin": "admin"}
        self.dicoactu = None
        self.mort = None
        self.defausse = None
        self.listemort = []
        self.dictionnaire = {"garde": 5, "pretre": 2, "Baron": 2, "servante": 2, "prince": 2, "roi": 1, "comtesse": 1,
                             "princesse": 1}
        self.valeur_carte = {"garde": 1, "pretre": 2, "Baron": 3, "servante": 4, "prince": 5, "roi": 6, "comtesse": 7,
                             "princesse": 8}

    def initialisation(self):
        for i in range(self.nbjoueur):
            self.dicoinfo[str(i)] = self.choix(self.dicoinfo)
        print(self.dicoinfo)
    """def start(self):
        dicoinfoini = self.dicoinfo.copy()

        while len(self.dicoinfo) > 1:
            for nom, role in dicoinfoini.items():
                self.dictmort = self.act(self.dicoinfo, role, nom, self.partie, self.dictmort).getdicomort()
                if list(self.dictmort.values())[-1] != "admin":
                    self.mort = list(self.dictmort.values())[-1]
                print(self.dicoinfo)
                print(nom)
                print(role)

                if nom in list(self.dicoinfo.keys()):

                    pioche = self.choix(self.dicoinfo)
                    # demander quel carte piocher
                    inter = Interface()
                    inter.run(nom, pioche, self.dicoinfo)
                    carte = inter.getchoix()
                    if carte == pioche:
                        ACT = self.act(self.dicoinfo, pioche, nom, self.partie, self.dictmort)
                        self.dicoinfo, self.dicoactu, self.defausse = ACT.action1()
                    if carte == role:
                        self.dicoinfo[nom] = pioche
                        ACT = self.act(self.dicoinfo, role, nom, self.partie, self.dictmort)
                        self.dicoinfo, self.dicoactu, self.defausse = ACT.action1()

                    self.dictmort.update(self.dicoactu)
                    print(self.dictmort)

        print("fin de partie")
        if len(self.dicoinfo) == 1:
            print("trop fort " + str(self.dicoinfo.keys()) + " a gagné la partie")
        if len(self.dicoinfo) == 0:
            print("mentalité de perdant")"""

    def jouer(self, joueur, role, joueurcible=None, rolecible=None):
        print(role+ " eziojzz")
        if role == "garde":
            if self.dicoinfo[str(joueurcible)] == rolecible:
                print(str(joueurcible) + " est éliminé")
                del self.dicoinfo[str(joueurcible)]
                self.listemort.append(joueurcible)
        if role == "pretre":
            print("le role du joueur " + str(joueurcible) + " est " + self.dicoinfo[str(joueurcible)])
        if role == "Baron":
            # demander de choisir un joueur
            if self.valeur_carte[role] > self.valeur_carte[self.dicoinfo[str(joueurcible)]]:
                self.listemort.append(joueurcible)
                del self.dicoinfo[str(joueurcible)]
                print(str(joueurcible) + " est éliminé")
            elif self.valeur_carte[self.dicoinfo[str(joueurcible)]] is not None:
                if self.valeur_carte[role] < self.valeur_carte[self.dicoinfo[str(joueurcible)]]:
                    self.listemort.append(joueur)
                    del self.dicoinfo[str(joueur)]
                    print(str(joueur) + " est éliminé")
        if role == "servante":
            pass
        if role == "comtesse":
            pass
        if role == "princesse":
            self.listemort.append(joueur)
            del self.dicoinfo[str(joueur)]
            print(str(joueur) + " est éliminé")
        if role == "prince":
            defausse = self.dicoinfo[str(joueurcible)]
            self.dicoinfo[str(joueurcible)] = self.choix(self.dicoinfo)
            print(str(joueurcible) + " a défaussé" + defausse)
            if defausse == "princesse":
                print(str(joueurcible) + " est éliminé")
                self.listemort.append(joueurcible)
                del self.dicoinfo[str(joueurcible)]
        if role == "roi":
            self.dicoinfo[str(joueur)] = self.dicoinfo[str(joueurcible)]
            self.dicoinfo[str(joueurcible)] = role
            print(str(joueurcible) + " et " + str(joueur) + " ont échangé leur main")
        print(self.listemort)
        return self.dicoinfo, self.listemort

    def getdicoinfo(self):
        return self.dicoinfo

    def changemainetpioche(self, joueur, mainjoue, pioche):
        self.dicoinfo[str(joueur)] = pioche
        print(mainjoue)
        print(self.dicoinfo)
    def choix(self, dico=None):
        """ if len(list(self.dictionnaire.keys())) == 0:
            v = 0
            print("la partie est finito")
            gagnant = None
            gagnant2 = None
            print(dico)
            for key, val in dico.items():
                valeur = self.valeur_carte[val]
                if valeur > v:
                    v = valeur
                    gagnant = key + " a gagné avec " + val
                    gagnant2 = None
                elif valeur == v:
                    gagnant2 = key + " a également gagné avec " + val
            print(gagnant)
            if gagnant2 is not None:
                print(gagnant2)
            exit()"""
        n = rd.choice(list(self.dictionnaire.keys()))
        self.dictionnaire[n] -= 1
        print(self.dictionnaire)
        self.role = n
        if self.dictionnaire[n] == 0:
            del self.dictionnaire[n]
        return self.role

    def getlistemort(self):
        return self.listemort
