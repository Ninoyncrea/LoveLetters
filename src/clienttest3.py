import socket
import pickle
import pygame
import threading


class ClientJeu:
    def __init__(self, server_host, server_port):
        self.SERVER_HOST = server_host
        self.SERVER_PORT = server_port

        # Initialiser Pygame
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.clock = pygame.time.Clock()

        # Créer un socket TCP/IP
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Se connecter au serveur
        self.client_socket.connect((self.SERVER_HOST, self.SERVER_PORT))
        print("Connecté au serveur.")

        # Démarrer le thread pour recevoir les données du serveur en arrière-plan
        self.receive_thread = threading.Thread(target=self.receive_data)
        self.receive_thread.start()

        # Charger les images de fond
        self.background_image = pygame.image.load("taverneV2.jpg")
        self.background_image = pygame.transform.scale(self.background_image, (800, 600))

        # Définir les variables pour les images des boutons
        self.button_images = ["facecache.jpg", "facecache.jpg", "facecache.jpg", "facecache.jpg"]
        self.right_button_images_paths = ["facecache.jpg", "facecache.jpg", "facecache.jpg", "facecache.jpg"]
        self.bottom_button_images = ["garde.jpg", "pretre.jpg", "Baron.jpg", "servante.jpg", "prince.jpg", "roi.jpg",
                                     "comtesse.jpg", "princesse.jpg"]

        # Positionner les boutons
        self.button_rects = [
            pygame.Rect(50, 275, 124, 174),
            pygame.Rect(325, 50, 124, 174),
            pygame.Rect(600, 275, 124, 174),
            pygame.Rect(325, 450, 124, 174)
        ]

        self.new_button_rects = [
            pygame.Rect(250, 275, 124, 174),
            pygame.Rect(525, 50, 124, 174),
            pygame.Rect(800, 275, 124, 174),
            pygame.Rect(525, 450, 124, 174)
        ]

        self.new_bottom_button_rects = [
            pygame.Rect(0, 625, 124, 174),
            pygame.Rect(150, 625, 124, 174),
            pygame.Rect(300, 625, 124, 174),
            pygame.Rect(450, 625, 124, 174),
            pygame.Rect(600, 625, 124, 174),
            pygame.Rect(750, 625, 124, 174),
            pygame.Rect(900, 625, 124, 174),
            pygame.Rect(1050, 625, 124, 174)
        ]
        self.right_button_rect = pygame.Rect(900, 250, 150, 150)  # Par exemple

        # Charger l'image du bouton
        self.right_button_image = pygame.image.load(
            "regle.jpg").convert_alpha()  # Remplacez par le nom de votre image

        # À l'intérieur de la boucle while dans la méthode run()
        # Dessiner le bouton sur la surface de l'écran
        self.screen.blit(self.right_button_image, self.right_button_rect)
    def receive_data(self):
        while True:
            data = self.client_socket.recv(4096)
            if not data:
                continue
            try:
                button_imag, right_button_images_path, id_client1 = pickle.loads(data)
                return button_imag, right_button_images_path, id_client1
            except EOFError:
                print("Erreur: Données incomplètes. Attente de plus de données.")
                continue

    def send_action(self, action):
        self.client_socket.sendall(action.encode())

    def load_button_images(self, button_images):
        return [pygame.image.load(image_path).convert_alpha() for image_path in button_images]

    def run(self):
        running = True
        cartejoue = ""
        joueurcible = None
        role = None
        while running:
            button_images, right_button_images_paths, id_client = self.receive_data()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print(event.pos)
                    for idx, rect in enumerate(self.button_rects):
                        if rect.collidepoint(event.pos):
                            if idx == id_client:
                                cartejoue = button_images[idx][:-4]
                            if idx != id_client:
                                joueurcible = idx
                    for idx, rect in enumerate(self.new_button_rects):
                        if rect.collidepoint(event.pos):
                            if idx == id_client:
                                cartejoue = right_button_images_paths[idx][:-4]
                    for idx, rect in enumerate(self.new_bottom_button_rects):
                        if rect.collidepoint(event.pos):
                            role = self.bottom_button_images[idx][:-4]
            if cartejoue == "princesse" or cartejoue == "comtesse" or cartejoue == "servante":
                chaine = str(id_client) + str(cartejoue)
                self.send_action(chaine)
                cartejoue = ""
            if (
                    cartejoue == "pretre" or cartejoue == "prince" or cartejoue == "Baron" or cartejoue == "roi") and joueurcible is not None:
                chaine = str(id_client) + str(cartejoue) + " " + str(joueurcible)
                self.send_action(chaine)
                cartejoue = ""
            if cartejoue == "garde" and joueurcible is not None and role is not None:
                chaine = str(id_client) + str(cartejoue) + " " + str(joueurcible) + " " + str(role)
                self.send_action(chaine)
                cartejoue = ""
            self.screen.blit(self.background_image, (0, 0))

            button_images_surface = self.load_button_images(button_images)
            for image, rect in zip(button_images_surface, self.button_rects):
                if image != "test":
                    self.screen.blit(image, rect)
            right_button_images_surface = self.load_button_images(right_button_images_paths)
            liste = [0, 1, 2, 3]
            compteur = 0
            for image, rect in zip(right_button_images_surface, self.new_button_rects):
                if right_button_images_paths[liste[compteur]] != "taverneV2.jpg":
                    self.screen.blit(image, rect)
                compteur += 1
            bottom_button_images_surface = self.load_button_images(self.bottom_button_images)
            for image, rect in zip(bottom_button_images_surface, self.new_bottom_button_rects):
                self.screen.blit(image, rect)
            pygame.display.flip()
            self.clock.tick(60)

        # Fermer la connexion avec le serveur
        self.client_socket.close()


# Utilisation de la classe ClientJeu
if __name__ == "__main__":
    SERVER_HOST = open("src/Master_ip.txt", "r").read().strip()
    SERVER_PORT = 5555
    client_jeu = ClientJeu(SERVER_HOST, SERVER_PORT)
    client_jeu.run()
