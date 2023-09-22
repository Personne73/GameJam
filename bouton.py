import pygame as pg

# Initialisation de Pygame
pg.init()

# Définir les couleurs
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Créer une fenêtre
window_size = (800, 600)
screen = pg.display.set_mode(window_size)

# Définir les dimensions et la position du bouton
button_rect = pg.Rect(300, 200, 200, 50)

# Boucle principale
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:  # Clic gauche de la souris
                if button_rect.collidepoint(event.pos):
                    print("Bouton cliqué")  # Ajoutez ici le code que vous souhaitez exécuter lorsque le bouton est cliqué

    # Effacer l'écran
    screen.fill(BLACK)

    # Dessiner le bouton
    pg.draw.rect(screen, GREEN, button_rect)

    # Mettre à jour l'affichage
    pg.display.flip()

# Quitter Pygame
pg.quit()
