import random as rd


class Character:
    def __init__(self):
        self.role = None
        self.dictionnaire = {"garde": 5, "pretre": 2, "Baron": 2, "servante": 2, "prince": 2, "roi": 1, "comtesse": 1,
                             "princesse": 1}
        self.nbrole = sum(self.dictionnaire.values())
        self.nbtyperole = len(self.dictionnaire) - 1

    def choix(self):
        if len(self.dictionnaire)<=0:
            print("fin de partie")
            return self.role
        n = rd.choice(list(self.dictionnaire.keys()))
        self.dictionnaire[n] -= 1
        print(self.dictionnaire)

        self.role = n
        if self.dictionnaire[n] == 0:
            del self.dictionnaire[n]
        return self.role

    def getnbrole(self):
        return self.nbrole


