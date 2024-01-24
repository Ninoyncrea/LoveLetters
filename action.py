from character import partie, J1role1, J2role1
from PyInquirer import prompt


class action:
    def __init__(self, listejoueur, listerole, role):
        self.listerole = listerole
        self.listejoueur = listejoueur
        self.role = role
    def action1(self):
        if self.role == "garde":
            cible = {
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
            }
        self.role = partie.choix()


Act = action(["J1", "J2"], ["roi", "baron"], ["garde"])
