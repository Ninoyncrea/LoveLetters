import random as rd


class Action:
    def __init__(self, dicoinfo, role, joueur, partie):
        self.dicoinfo = dicoinfo
        self.role = role
        self.joueur = joueur
        self.valeur_carte = {"garde": 1, "pretre": 2, "Baron": 3, "servante": 4, "prince": 5, "roi": 6, "comtesse": 7,
                             "princesse": 8}
        self.partie = partie

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
            demandeutilisateur = rd.choice(list(self.dicoinfo.keys()))
            demanderole = ""
            if demanderole == self.dicoinfo[demandeutilisateur]:
                del self.dicoinfo[demandeutilisateur]
        if self.role == "pretre":
            # interface choisir un joueur
            demandeutilisateur = rd.choice(list(self.dicoinfo.keys()))
            print(self.dicoinfo[demandeutilisateur])
        if self.role == "Baron":
            # demander de choisir un joueur
            demandeutilisateur = rd.choice(list(self.dicoinfo.keys()))
            if self.valeur_carte[self.role] > self.valeur_carte[self.dicoinfo[demandeutilisateur]]:
                del self.dicoinfo[demandeutilisateur]
                print(demandeutilisateur + " est éliminé")

            if self.valeur_carte[self.role] < self.valeur_carte[self.dicoinfo[demandeutilisateur]]:
                del self.dicoinfo[self.joueur]
                print(self.joueur + " est éliminé")
        if self.role == "prince":
            demandeutilisateur = rd.choice(list(self.dicoinfo.keys()))
            self.dicoinfo[demandeutilisateur] = self.partie.choix()
        if self.role == "roi":
            # interface de choisir joueur
            demandeutilisateur = rd.choice(list(self.dicoinfo.keys()))
            self.dicoinfo[self.joueur] = self.dicoinfo[demandeutilisateur]
            self.dicoinfo[self.joueur] = self.role
        if self.role == "princesse":
            del self.dicoinfo[self.joueur]
            print(self.joueur)
        if len(self.dicoinfo) == 1:
            print("la partie est fini")
        return self.dicoinfo

