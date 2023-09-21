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

        # Create the play button
        icon_play_button_path = os.path.join("images", "menu_play_button.png")
        icon_play_button_hovered_path = os.path.join("images", "menu_play_button_hover.png")
        self.icon_play_button = IconButton(icon_play_button_path, icon_play_button_hovered_path, self.width // 2, 3 * self.height // 4, self.screen)

        # Create the sound button
        icon_sound_button_path = os.path.join("images", "music_icon.png")
        icon_sound_button_hovered_path = os.path.join("images", "music_icon_disabled.png")
        self.icon_sound_button = IconButton(icon_sound_button_path, icon_sound_button_hovered_path, 80, 40, self.screen)
        self.pause = False

    def load_image(self, image_path, x, y):
        image = pg.image.load(image_path)
        rect = image.get_rect()
        rect.center = (x, y)
        self.screen.blit(image, rect)

    def play_music(self, music_path):
        pg.mixer.music.load(music_path)
        pg.mixer.music.play(-1)  # -1 means that the music will be played in loop

    def draw(self):
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

        # Draw the sound button
        self.icon_sound_button.draw_icon()

    def handle_events(self):
        if self.icon_play_button.is_clicked():
            pg.mixer.music.stop()
        if self.icon_sound_button.is_clicked():
            if self.pause:
                pg.mixer.music.unpause()
                self.icon_sound_button.draw_icon()
                self.pause = False
            else:
                pg.mixer.music.pause()
                self.icon_sound_button.draw_hovered()
                self.pause = True
        if self.icon_play_button.is_hovered() or not self.icon_play_button.is_hovered():
            self.icon_play_button.switch_icon()

    


def main():
    pg.init()
    window_size = (560, 800)
    screen = pg.display.set_mode(window_size)
    game_over = False

    clock_framerate = pg.time.Clock()

    high_score = 1000

    # Create the menu
    menu = Menu(screen)
    menu.draw()
    menu.play_music(os.path.join("sounds", "menu_music.mp3"))

    while not game_over:
        for event in pg.event.get():
            menu.handle_events()
            if event.type == pg.QUIT:
                game_over = True
                pg.mixer.music.stop()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    game_over = True


        FRAMERATE = 60

        pg.display.flip()
        clock_framerate.tick(FRAMERATE)

    pg.quit()


if __name__ == "__main__":
    main()
