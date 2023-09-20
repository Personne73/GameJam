import pygame as pg
import main

class Player(pg.sprite.Sprite):
    def __init__(self, image_path: str):
        super().__init__()
        self.image_avancer = pg.image.load(image_path + "player_z.png").convert_alpha()
        self.image_reculer = pg.image.load(image_path + "player_s.png").convert_alpha()
        self.image_gauche = pg.image.load(image_path + "player_q.png").convert_alpha()
        self.image_droite = pg.image.load(image_path + "player_d.png").convert_alpha()

        self.images = {
            (0, -1): self.image_avancer,  # Vers le haut (direction y négative)
            (0, 1): self.image_reculer,  # Vers le bas (direction y positive)
            (-1, 0): self.image_gauche,  # Vers la gauche (direction x négative)
            (1, 0): self.image_droite,  # Vers la droite (direction x positive)
        }

        self.image = self.image_avancer
        self.mask = pg.mask.from_surface(self.image)


        self.position = [7, 15]
        self.rect = self.image.get_rect()
        self.x = self.position[0] * main.CASE_SIZE  # Position initiale en pixels (6ème colonne)
        self.y = self.position[1] * main.CASE_SIZE  # Position initiale en pixels (dernière ligne)


    def update(self, car_group):
        self.check_collision(car_group)
        self.rect.topleft = (self.x, self.y)
        
    def move (self, direction):
        # Vérifier si le déplacement est valide
        new_x = self.x + direction[0] * main.CASE_SIZE
        new_y = self.y + direction[1] * main.CASE_SIZE
        if 0 <= new_x < main.WINDOW_SIZE[0] and 0 <= new_y < main.WINDOW_SIZE[1]:
            self.x = new_x
            self.y = new_y
        self.image = self.images.get(direction, self.image)

    def check_collision(self, car_group):
        car_check = pg.sprite.spritecollide(self, car_group, False, pg.sprite.collide_mask)
        if car_check:
            main.GAME_OVER = True

        
    # def isBlocked(self, terrain):
    #     if terrain[]
