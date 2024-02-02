import pygame
import sys


class Fenetre:
    def __init__(self):
        pygame.init()
        self.WHITE = (255, 255, 255)
        self.num = 0

    def afficher_boutons_joueurs(self, noms_joueurs, dicomort, nom, pioche=None):
        # Initialisation de Pygame
        # Définir la taille de la fenêtre
        largeur, hauteur = 800, 600
        fenetre = pygame.display.set_mode((largeur, hauteur))
        pygame.display.set_caption("Boutons Joueurs")

        # Charger l'image du bouton

        image_bouton = pygame.image.load('facecache.jpg')

        # Obtenir les dimensions de l'image du bouton
        largeur_bouton, hauteur_bouton = image_bouton.get_size()

        # Définir la couleur du bouton lorsqu'il est survolé
        couleur_survol = (200, 200, 200)

        # Définir la police pour le texte explicatif
        police = pygame.font.Font(None, 36)

        # Position de départ pour les boutons
        x_bouton, y_bouton = 50, 150
        if self.num > len(noms_joueurs):
            self.num = 0
        # Espacement entre les boutons
        espacement_boutons = 40
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
                path = dicomort[i] + ".jpg"
                image = pygame.image.load(path)
                fenetre.blit(image, (x_bouton, y_bouton))
                # Mettre à jour les coordonnées pour le prochain bouton
                x_bouton += largeur_bouton + espacement_boutons

        if pioche != None:
            print(pioche)
            texte_explicatif = police.render("défausse", True, (0, 0, 0))
            fenetre.blit(texte_explicatif, (x_bouton, y_bouton - 150))
            # Obtenir les coordonnées de la souris
            image = pygame.image.load(pioche + ".jpg")
            fenetre.blit(image, (x_bouton, y_bouton))
        if pioche == None:
            print(pioche)
            texte_explicatif = police.render("défausse", True, (0, 0, 0))
            fenetre.blit(texte_explicatif, (x_bouton, y_bouton + 150))
            # Obtenir les coordonnées de la souris
            fenetre.blit(image_bouton, (x_bouton, y_bouton + 200))

        largeur_bouton_jouer, hauteur_bouton_jouer = 180, 40  # Ajustez la taille du bouton "Jouer"
        x_bouton_jouer, y_bouton_jouer = 350, 500  # Ajustez la position du bouton "Jouer"
        pygame.draw.rect(fenetre, (0, 128, 255),
                         (x_bouton_jouer, y_bouton_jouer, largeur_bouton_jouer, hauteur_bouton_jouer))
        police_bouton = pygame.font.Font(None, 36)
        texte_bouton = police_bouton.render("à "+nom+ " de Jouer", True, (255, 255, 255))
        fenetre.blit(texte_bouton, (x_bouton_jouer + 10, y_bouton_jouer + 10))
        pygame.display.flip()
        self.num += 1

        # Boucle principale
        running = True
        while running:
            pygame.event.pump()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouseX, mouseY = pygame.mouse.get_pos()
                    # Vérification si le clic est sur le bouton "Jouer"
                    if x_bouton_jouer <= mouseX <= x_bouton_jouer + largeur_bouton_jouer and \
                            y_bouton_jouer <= mouseY <= y_bouton_jouer + hauteur_bouton_jouer:
                        running = False

    def affichevainqueur(self, nom):
        pygame.init()

        # Définition des couleurs
        blanc = (255, 255, 255)
        noir = (0, 0, 0)

        # Taille de la fenêtre
        largeur, hauteur = 800, 600

        # Création de la fenêtre
        fenetre = pygame.display.set_mode((largeur, hauteur))
        pygame.display.set_caption("Fenêtre Magnifique")

        # Fonction pour afficher le message de victoire
        font = pygame.font.Font(None, 36)
        message = font.render(f"{nom} a gagné la partie!", True, blanc)
        rect = message.get_rect(center=(largeur // 2, hauteur // 2))

        # Boucle principale
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Effacer l'écran
            fenetre.fill(noir)

            # Afficher le message de victoire
            fenetre.blit(message, rect.topleft)
            # Remplacez "Joueur1" par le nom réel du gagnant

            # Mettre à jour l'affichage
            pygame.display.flip()

        # Quitter Pygame
        pygame.quit()
        sys.exit()
