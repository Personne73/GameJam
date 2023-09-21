import os
import pygame as pg


class IconButton:
    def __init__(self, icon_path, hovered_icon_path, x, y, screen):
        self.icon = pg.image.load(icon_path)
        self.hovered_icon = pg.image.load(hovered_icon_path)
        self.rect = self.icon.get_rect()
        self.rect.center = (x, y)
        self.screen = screen

        self.screen.blit(self.icon, self.rect)


    def draw_icon(self):
        self.screen.blit(self.icon, self.rect)

    def draw_hovered(self):
        self.screen.blit(self.hovered_icon, self.rect)

    def is_clicked(self):
        # Recover the mouse position
        mouse_pos = pg.mouse.get_pos()

        # Check if the mouse is over the button and if the left button is pressed
        if self.rect.collidepoint(mouse_pos) and pg.mouse.get_pressed()[0]:
            return True

        return False
    def is_hovered(self):
        mouse_pos = pg.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            return True
        
        return False
    
    def switch_icon(self):
        if self.is_hovered():
            self.draw_hovered()
        elif not self.is_hovered():
            self.draw_icon()


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = screen.get_size()
        icon_play_button_path = os.path.join("images", "menu_play_button.png")
        icon_play_button_hovered_path = os.path.join("img", "menu_play_button_hover.png")
        self.icon_play_button = IconButton(icon_play_button_path, icon_play_button_hovered_path, self.width // 2, 3 * self.height // 4, self.screen)

    def load_image(self, image_path, x, y):
        image = pg.image.load(image_path)
        rect = image.get_rect()
        rect.center = (x, y)
        self.screen.blit(image, rect)

    def draw(self, high_score):
        # Draw the background
        # self.screen.fill((0, 0, 0))  # Background color (black)
        background_image_path = os.path.join("images", "menu_background.png")
        self.load_image(background_image_path, self.width // 2, self.height // 2)

        # Draw the logo
        logo_image_path = os.path.join("images", "menu_logo.png")
        self.load_image(logo_image_path, self.width // 2, self.height // 2)

        # Draw the play button
        self.icon_play_button.draw_icon()

        # Draw the high score
        self.draw_high_score(high_score)

    def draw_high_score(self, high_score):
        SMALL_FONT = 15
        MEDIUM_FONT = 15
        BIG_FONT = 25

        crossy_font_big = pg.font.Font('fonts/8-BIT WONDER.TTF', BIG_FONT)
        crossy_font_small = pg.font.Font('fonts/8-BIT WONDER.TTF', SMALL_FONT)

        font = pg.font.Font(crossy_font_big, 36)  # Sélectionnez la police et la taille de la police
        text = font.render(f"High Score: {high_score}", True, (255, 255, 255))  # Créez un objet texte avec le score
        text_rect = text.get_rect()
        text_rect.center = (self.width // 2, 50)  # Centrez le texte en haut de la fenêtre
        self.screen.blit(text, text_rect)  # Affichez le texte sur l'écran


    def handle_events(self):
        if self.icon_play_button.is_clicked():
            print("Start button clicked")
        if self.icon_play_button.is_hovered():
            self.icon_play_button.switch_icon()
            print("hovered")
        if not self.icon_play_button.is_hovered():
            self.icon_play_button.switch_icon()
            print("not hovered")

    


def main():
    pg.init()
    window_size = (560, 800)
    screen = pg.display.set_mode(window_size)
    game_over = False

    clock_framerate = pg.time.Clock()

    high_score = 1000

    # Create the menu
    menu = Menu(screen)
    menu.draw(high_score)

    while not game_over:
        for event in pg.event.get():
            menu.handle_events()
            if event.type == pg.QUIT:
                game_over = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    game_over = True


        FRAMERATE = 60

        pg.display.flip()
        clock_framerate.tick(FRAMERATE)

    pg.quit()


if __name__ == "__main__":
    main()