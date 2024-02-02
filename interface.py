import pygame
import sys


class Interface:
    def __init__(self):
        # Initialisation de Pygame
        pygame.init()
        self.choix = None
        # Définition de couleurs
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

        # Paramètres de la fenêtre principale
        self.WIDTH, self.HEIGHT = 400, 300
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Nombre de Joueurs")

        # Police de texte
        self.font = pygame.font.Font(None, 36)


        # Nombre de joueurs
        self.num_players = 0

    def ask_players(self):
        # Boucle pour la saisie du nombre de joueurs
        input_text = ""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        try:
                            # Essayer de convertir le texte en nombre
                            self.num_players = int(input_text)
                            return self.num_players
                        except ValueError:
                            # En cas d'erreur de conversion, réinitialiser le texte
                            input_text = ""
                    elif event.key == pygame.K_BACKSPACE:
                        # Supprimer le dernier caractère du texte
                        input_text = input_text[:-1]
                    else:
                        # Ajouter le caractère tapé au texte
                        input_text += event.unicode

            # Effacer l'écran
            self.screen.fill(self.WHITE)

            # Afficher le texte de saisie
            text_surface = self.font.render("Nombre de joueurs : " + input_text, True, self.BLACK)
            self.screen.blit(text_surface, (50, 100))

            # Rafraîchir l'affichage
            pygame.display.flip()

    def create_buttons_window(self, role, role2, nom):
        # Créer une nouvelle fenêtre avec deux boutons
        self.background = pygame.image.load("taverneV2.jpg")
        # Redimensionne l'image pour s'adapter à la taille de l'écran
        self.background = pygame.transform.scale(self.background, (self.WIDTH, self.HEIGHT))
        self.screen.blit(self.background, (0, 0))
        button_width, button_height = 174, 174
        button_spacing = 55
        button_margin_top = 50
        self.WIDTH, self.HEIGHT = 700, 350

        window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("fenêtre d'action de " + nom)

        # Créer les boutons
        button1_rect = pygame.Rect(0, button_margin_top, button_width, button_height)
        button2_rect = pygame.Rect(button_width + button_spacing, button_margin_top, button_width, button_height)
        font = pygame.font.Font(None, 24)
        label1 = font.render(role, True, self.BLACK)
        label2 = font.render(role2, True, self.BLACK)

        # Positionner les labels au-dessus des boutons
        label1_rect = label1.get_rect(center=(button1_rect.centerx, button1_rect.top - 15))
        label2_rect = label2.get_rect(center=(button2_rect.centerx, button2_rect.top - 15))
        return window, button1_rect, button2_rect, label1, label2, label1_rect, label2_rect


    def run(self, nom, role, dicoinfo):
        # Appeler la fonction pour demander le nombre de joueurs
        # Créer la fenêtre avec les deux boutons
        button_window, button1, button2, label1, label2, label1_rect, label2_rect = self.create_buttons_window(role,
                                                                                                               dicoinfo[
                                                                                                                   nom],
                                                                                                               nom)
        button_window.fill(self.WHITE)
        pygame.draw.rect(button_window, self.BLACK, button1)
        pygame.draw.rect(button_window, self.BLACK, button2)
        button_window.fill(self.WHITE)
        pygame.draw.rect(button_window, self.BLACK, button1)
        pygame.draw.rect(button_window, self.BLACK, button2)
        button_window.blit(label1, label1_rect)
        button_window.blit(label2, label2_rect)
        button1_image = pygame.image.load(role + ".jpg")
        button2_image = pygame.image.load(dicoinfo[nom] + ".jpg")
        button_window.blit(button1_image, button1)
        button_window.blit(button2_image, button2)
        button_image = pygame.image.load("regle1.jpg")
        button_rect = button_image.get_rect(topleft=(430, 0))
        # Rafraîchir l'affichage de la fenêtre avec les boutons et l'image
        button_window.blit(button_image, button_rect)
        # Rafraîchir l'affichage de la fenêtre avec les boutons
        pygame.display.flip()
        # Boucle principale pour la fenêtre avec les boutons
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Vérifier si un bouton est cliqué
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button1.collidepoint(event.pos):
                        print(role)
                        self.choix = role
                        pygame.quit()
                        return
                    elif button2.collidepoint(event.pos):
                        print(dicoinfo[nom])
                        self.choix = dicoinfo[nom]
                        pygame.quit()
                        return
            # Dessiner les boutons sur la fenêtre avec les boutons

    def choix_joueur(self, dicoinfo):
        liste_elements = list(dicoinfo.keys())
        element_select = None
        # Boucle pour la sélection d'un élément
        selected_index = 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        # L'utilisateur a choisi l'élément actuellement sélectionné
                        element_select = liste_elements[selected_index]
                        return element_select
                    elif event.key == pygame.K_UP:
                        # Déplacer la sélection vers le haut
                        selected_index = (selected_index - 1) % len(liste_elements)
                    elif event.key == pygame.K_DOWN:
                        # Déplacer la sélection vers le bas
                        selected_index = (selected_index + 1) % len(liste_elements)

            # Effacer l'écran
            self.screen.fill(self.WHITE)

            # Afficher les éléments de la liste
            for i, element in enumerate(liste_elements):
                color = self.BLACK if i == selected_index else (100, 100, 100)
                text_surface = self.font.render(element, True, color)
                text_rect = text_surface.get_rect(center=(self.WIDTH // 2, 50 + i * 50))
                self.screen.blit(text_surface, text_rect)

            # Rafraîchir l'affichage
            pygame.display.flip()

    def getchoix(self):
        return self.choix

    def elimine(self, irrevocable):
        # Afficher une nouvelle fenêtre "Joueur 1 éliminé"
        elimination_window = pygame.display.set_mode((300, 200))
        pygame.display.set_caption("Élimination")
        elimination_window.fill(self.WHITE)
        # Afficher le texte dans la nouvelle fenêtre
        font = pygame.font.Font(None, 24)
        text_surface = font.render(irrevocable + "est éliminé!", True, self.BLACK)
        text_rect = text_surface.get_rect(center=(150, 100))
        elimination_window.blit(text_surface, text_rect)

        # Rafraîchir l'affichage de la nouvelle fenêtre
        pygame.display.flip()

        # Attendre quelques secondes avant de fermer automatiquement la nouvelle fenêtre
        pygame.time.wait(3000)
        pygame.quit()

    def pretre(self, irrevocable, nom):
        # Afficher une nouvelle fenêtre "Joueur 1 éliminé"
        elimination_window = pygame.display.set_mode((300, 200))
        pygame.display.set_caption("prêtre")
        elimination_window.fill(self.WHITE)
        # Afficher le texte dans la nouvelle fenêtre
        font = pygame.font.Font(None, 24)
        text_surface = font.render("le role de " + nom + " est : " + irrevocable, True, self.BLACK)
        text_rect = text_surface.get_rect(center=(150, 100))
        elimination_window.blit(text_surface, text_rect)

        # Rafraîchir l'affichage de la nouvelle fenêtre
        pygame.display.flip()

        # Attendre quelques secondes avant de fermer automatiquement la nouvelle fenêtre
        pygame.time.wait(3000)
        pygame.quit()
