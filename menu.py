import pygame as pg

class Menu:
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    BRIGHT_GREEN = (0, 200, 0)

    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = screen.get_size()
        self.font = pg.font.Font(None, 36)
        self.start_button = Button(self.width // 4, self.height // 2 - 50, self.width // 2, 50, "Start", Menu.GREEN, self.screen)
        # self.high_score_button = pg.Rect(self.width // 4, self.height // 2 + 50, self.width // 2, 50)

    def draw(self):
        # Dessiner le fond du menu
        self.screen.fill((0, 0, 0))  # Couleur de fond (noir)

        # Dessiner le bouton "Start"
        self.start_button.draw(self.screen)

    def handle_events(self):
        for event in pg.event.get():
            self.start_button.is_hovered()
            if event.type == pg.MOUSEBUTTONDOWN:
                self.start_button.is_clicked()
                

class Button:
    # # Définir les couleurs
    # BLACK = (0, 0, 0)
    # GREEN = (0, 255, 0)
    # BRIGHT_GREEN = (0, 200, 0)
    
    # # Définir les dimensions et la position du bouton
    # button_rect = pg.Rect(300, 200, 200, 50)
    # running = True
    # while running:
    #     for event in pg.event.get():
    #         if event.type == pg.QUIT:
    #             running = False
    #         if event.type == pg.MOUSEBUTTONDOWN:
    #             if event.button == 1:  # Clic gauche de la souris
    #                 if button_rect.collidepoint(event.pos):
    #                     print("Bouton cliqué")  # Ajoutez ici le code que vous souhaitez exécuter lorsque le bouton est cliqué

    # # Vérifier si la souris survole le bouton
    # if button_rect.collidepoint(pg.mouse.get_pos()):
    #     hovered = True
    # else:
    #     hovered = False

    # # Effacer l'écran
    # screen.fill(BLACK)

    # # Dessiner le bouton avec une couleur différente s'il est survolé
    # if hovered:
    #     pg.draw.rect(screen, BRIGHT_GREEN, button_rect)
    # else:
    #     pg.draw.rect(screen, GREEN, button_rect)

    # # Mettre à jourr l'affichage
    # pg.display.flip()

    def __init__(self, x, y, width, height, text, color, screen):
        self.rect = pg.Rect(x, y, width, height)
        self.text = text
        self.screen = screen
        self.color = color

    def draw(self, screen):
        pg.draw.rect(self.screen, self.color, self.rect)
        font = pg.font.Font(None, 36)
        text = font.render(self.text, True, (0, 0, 0))
        text_rect = text.get_rect(center=self.rect.center)
        self.screen.blit(text, text_rect)

    def is_hovered(self):
        if self.rect.collidepoint(pg.mouse.get_pos()):
            hovered = True
            print("is hovered")
        else:
            hovered = False
        # mouse_pos = pg.mouse.get_pos()
        # return self.rect.collidepoint(mouse_pos)

    def is_clicked(self):     
        if self.collidepoint(pg.mouse.get_pos()):
            print("Start button clicked")  # Vous pouvez ajouter le code de démarrage du jeu ici
                   

def main():
    pg.init()
    window_size = (560, 800)
    screen = pg.display.set_mode(window_size)
    game_over = False
    
    clock_framerate = pg.time.Clock()
    menu = Menu(screen)

    while not game_over:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_over = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    game_over = True
        
        menu.handle_events()
        menu.draw()

        FRAMERATE =  60

        pg.display.flip()
        clock_framerate.tick(FRAMERATE)

    pg.quit()
    

if __name__ == "__main__":
    main()
