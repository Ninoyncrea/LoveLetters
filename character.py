import random as rd

class character:
    def __init__(self):
        self.role = None
        self.dictionnaire = {"garde": 5, "pretre": 2, "Baron": 2, "servante": 2, "prince": 2, "roi": 1, "comtesse": 1,
                             "princesse": 1}
        self.nbrole = sum(self.dictionnaire.values())
        self.nbtyperole = len(self.dictionnaire) - 1

    def choix(self):
        n = rd.choice(list(self.dictionnaire.keys()))
        self.dictionnaire[n] -= 1
        self.role = n
        if self.dictionnaire[n] == 0:
            del self.dictionnaire[n]
        print(self.dictionnaire)
        return self.role

partie = character()

J1role1 = partie.choix(), partie.choix()
J2role1 = partie.choix(), partie.choix()
print(J1role1)