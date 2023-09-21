import os
import pygame as pg


class IconButton:
    def __init__(self, icon_path, x, y, screen):
        self.icon = pg.image.load(icon_path)
        self.rect = self.icon.get_rect()
        self.rect.center = (x, y)
        self.screen = screen

    def draw(self):
        self.screen.blit(self.icon, self.rect)

    def is_clicked(self):
        # Recover the mouse position
        mouse_pos = pg.mouse.get_pos()

        # Check if the mouse is over the button and if the left button is pressed
        if self.rect.collidepoint(mouse_pos) and pg.mouse.get_pressed()[0]:
            return True

        return False


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = screen.get_size()
        icon_play_button_path = os.path.join("images", "menu_play_button.png")
        self.icon_play_button = IconButton(icon_play_button_path, self.width // 2, 3 * self.height // 4, self.screen)

    def load_image(self, image_path, x, y):
        image = pg.image.load(image_path)
        rect = image.get_rect()
        rect.center = (x, y)
        self.screen.blit(image, rect)

    def draw(self):
        # Draw the background
        # self.screen.fill((0, 0, 0))  # Background color (black)
        background_image_path = os.path.join("images", "menu_background.png")
        self.load_image(background_image_path, self.width // 2, self.height // 2)

        # Draw the logo
        logo_image_path = os.path.join("images", "menu_logo.png")
        self.load_image(logo_image_path, self.width // 2, self.height // 2)

        # Draw the play button
        self.icon_play_button.draw()

    def handle_events(self):
        if self.icon_play_button.is_clicked():
            print("Start button clicked")


def main():
    pg.init()
    window_size = (560, 800)
    screen = pg.display.set_mode(window_size)
    game_over = False

    clock_framerate = pg.time.Clock()

    # Create the menu
    menu = Menu(screen)
    menu.draw()

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