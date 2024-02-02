import pygame
import sys


class Fenetre:
    def __init__(self):
        pygame.init()
        self.WHITE = (255, 255, 255)

    def afficher_boutons_joueurs(self, noms_joueurs, dicomort, pioche=None):
        # Initialisation de Pygame
        print(dicomort)
        # Définir la taille de la fenêtre
        largeur, hauteur = 800, 600
        fenetre = pygame.display.set_mode((largeur, hauteur))
        pygame.display.set_caption("Boutons Joueurs")

        # Charger l'image du bouton

        image_bouton = pygame.image.load('garde.jpg')

        # Obtenir les dimensions de l'image du bouton
        largeur_bouton, hauteur_bouton = image_bouton.get_size()

        # Définir la couleur du bouton lorsqu'il est survolé
        couleur_survol = (200, 200, 200)

        # Définir la police pour le texte explicatif
        police = pygame.font.Font(None, 36)

        # Position de départ pour les boutons
        x_bouton, y_bouton = 50, 150

        # Espacement entre les boutons
        espacement_boutons = 20
        fenetre.fill(self.WHITE)
        for i, nom_joueur in noms_joueurs.items():
            if i != "admin":
                print(i)
                texte_explicatif = police.render(f"{i}", True, (0, 0, 0))
                fenetre.blit(texte_explicatif, (x_bouton, y_bouton - 50))
                # Obtenir les coordonnées de la souris

                fenetre.blit(image_bouton, (x_bouton, y_bouton))

                # Mettre à jour les coordonnées pour le prochain bouton
                x_bouton += largeur_bouton + espacement_boutons
        for i, nom_joueur in dicomort.items():
            if i != "admin":
                print(i)
                texte_explicatif = police.render(f"{i}", True, (0, 0, 0))
                fenetre.blit(texte_explicatif, (x_bouton, y_bouton - 50))
                # Obtenir les coordonnées de la souris
                fenetre.blit(dicomort[i] + ".jpg", (x_bouton, y_bouton))
                # Mettre à jour les coordonnées pour le prochain bouton
                x_bouton += largeur_bouton + espacement_boutons

        if pioche != None:
            print(pioche)
            texte_explicatif = police.render("pioche", True, (0, 0, 0))
            fenetre.blit(texte_explicatif, (x_bouton, y_bouton - 50))
            # Obtenir les coordonnées de la souris

            fenetre.blit(pioche + ".jpg", (x_bouton, y_bouton))
        if pioche == None:
            print(pioche)
            texte_explicatif = police.render("pioche", True, (0, 0, 0))
            fenetre.blit(texte_explicatif, (x_bouton, y_bouton - 50))
            # Obtenir les coordonnées de la souris
            fenetre.blit(image_bouton, (x_bouton, y_bouton))
        pygame.display.flip()
        running = True
        while running:
            pygame.event.pump()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

