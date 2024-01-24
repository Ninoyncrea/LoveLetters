from character import partie, J1role1, J2role1
from PyInquirer import prompt


class action:
    def __init__(self, dicoinfo, role, joueur):
        self.dicoinfo = dicoinfo
        self.role = role
        self.joueur = joueur
        self.valeur_carte = {"garde": 1, "pretre": 2, "Baron": 3, "servante": 4, "prince": 5, "roi": 6, "comtesse": 7,
                             "princesse": 8}
    def action1(self):
        if self.role == "garde":
           """ cible = { #Faire interface ici qui fait les propositions de choix
                'type': 'list',
                'name': 'choix de cible',
                'message': 'Sélectionnez un joueur',
                'choices': self.listejoueur,
            }
            reponse = prompt(cible)
            print(reponse["choix de cible"])
            cible = {
                'type': 'list',
                'name': 'choix de cible',
                'message': 'Sélectionnez un rôle',
                'choices': [self.listejoueur],
            }"""
        if self.role == "pretre":
             #interface choisir un joueur
            demandeutilisateur = ""
            print(self.dicoinfo[demandeutilisateur])
        if self.role == "Baron":
             #demander de choisir un joueur
            demandeutilisateur = ""
            if self.valeur_carte[self.joueur] > self.valeur_carte[demandeutilisateur]:
                del self.dicoinfo[demandeutilisateur]
            if self.valeur_carte[self.joueur] < self.valeur_carte[demandeutilisateur]:
                del self.dicoinfo[self.joueur]
        self.role = partie.choix()


Act = action(["J1", "J2"], ["roi", "baron"], ["garde"])
