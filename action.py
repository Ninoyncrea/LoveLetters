import random as rd
from interface import Interface


class Action:
    def __init__(self, dicoinfo, role, joueur, partie, dicomort):
        self.dicoinfo = dicoinfo
        self.role = role
        self.joueur = joueur
        self.valeur_carte = {"garde": 1, "pretre": 2, "Baron": 3, "servante": 4, "prince": 5, "roi": 6, "comtesse": 7,
                             "princesse": 8}
        self.partie = partie
        self.dicomort = dicomort

    def action1(self):
        inter = Interface()
        if self.role == "garde":
            demandeutilisateur = inter.choix_joueur(self.dicoinfo)
            valeur_cartesansgarde = self.valeur_carte.copy()
            del valeur_cartesansgarde["garde"]
            demanderole = inter.choix_joueur(valeur_cartesansgarde)
            if demanderole == self.dicoinfo[demandeutilisateur]:
                self.dicomort[demandeutilisateur] = demanderole
                del self.dicoinfo[demandeutilisateur]
                inter.elimine(demandeutilisateur)
        if self.role == "pretre":
            # interface choisir un joueur
            demandeutilisateur = inter.choix_joueur(self.dicoinfo)
            inter.pretre(self.dicoinfo[demandeutilisateur], demandeutilisateur)
            print(self.dicoinfo[demandeutilisateur])
        if self.role == "Baron":
            # demander de choisir un joueur
            demandeutilisateur = inter.choix_joueur(self.dicoinfo)
            if self.valeur_carte[self.role] > self.valeur_carte[self.dicoinfo[demandeutilisateur]]:
                self.dicomort[demandeutilisateur] = self.dicoinfo[demandeutilisateur]
                del self.dicoinfo[demandeutilisateur]
                inter.elimine(demandeutilisateur)
            if self.valeur_carte[self.dicoinfo[demandeutilisateur]] is not None:
                if self.valeur_carte[self.role] < self.valeur_carte[self.dicoinfo[demandeutilisateur]]:
                    self.dicomort[self.joueur] = self.dicoinfo[self.joueur]
                    del self.dicoinfo[self.joueur]
                    inter.elimine(self.joueur)
        if self.role == "v":
            pass
        if self.role == "prince":
            demandeutilisateur = inter.choix_joueur(self.dicoinfo)
            self.dicoinfo[demandeutilisateur] = self.partie.choix(self.dicoinfo)
        if self.role == "roi":
            # interface de choisir joueur
            demandeutilisateur = inter.choix_joueur(self.dicoinfo)
            self.dicoinfo[self.joueur] = self.dicoinfo[demandeutilisateur]
            self.dicoinfo[self.joueur] = self.role
        if self.role == "princesse":
            self.dicomort[self.joueur] = self.role
            del self.dicoinfo[self.joueur]
            inter.elimine(self.joueur)
        if len(self.dicoinfo) == 1:
            print("la partie est fini")
        return self.dicoinfo, self.dicomort

    def getdicomort(self):
        return self.dicomort
