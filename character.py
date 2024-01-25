import random as rd


class Character:
    def __init__(self):
        self.role = None
        self.dictionnaire = {"garde": 5, "pretre": 2, "Baron": 2, "servante": 2, "prince": 2, "roi": 1, "comtesse": 1,
                             "princesse": 1}
        self.nbrole = sum(self.dictionnaire.values())
        self.nbtyperole = len(self.dictionnaire) - 1
        self.valeur_carte = {"garde": 1, "pretre": 2, "Baron": 3, "servante": 4, "prince": 5, "roi": 6, "comtesse": 7,
                             "princesse": 8}

    def choix(self, dico):
        if len(list(self.dictionnaire.keys())) == 0:
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
            if gagnant2 != None:
                print(gagnant2)
            exit()
        n = rd.choice(list(self.dictionnaire.keys()))
        self.dictionnaire[n] -= 1
        print(self.dictionnaire)

        self.role = n
        if self.dictionnaire[n] == 0:
            del self.dictionnaire[n]
        return self.role

    def getnbrole(self):
        return self.nbrole
