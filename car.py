import pygame as pg
import random
import main

class Car(pg.sprite.Sprite):
    SKINS = []
    def __init__(self, image_path: str, direction: bool):
        super().__init__()
        self.direction = direction

        # Load the images only once
        if Car.SKINS == []:
            Car.SKINS = [
                pg.image.load(image_path + "blue_car.png").convert_alpha(),
                pg.image.load(image_path + "green_car.png").convert_alpha(),
                pg.image.load(image_path + "orange_car.png").convert_alpha(),
                pg.image.load(image_path + "pink_car.png").convert_alpha(),
                pg.image.load(image_path + "red_car.png").convert_alpha(),
                pg.image.load(image_path + "violet_car.png").convert_alpha(),
                pg.image.load(image_path + "yellow_car.png").convert_alpha()
            ]

        self.image = Car.SKINS[random.randint(0, len(Car.SKINS) - 1)]
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)
        self.rect.top = main.CASE_SIZE * 8
        if self.direction:
            self.image = pg.transform.flip(self.image, True, False)
            self.rect.left = main.WINDOW_SIZE[0]
        else:
            self.rect.left = - self.rect.w


    def update(self, speed):
        self.rect.left -= main.CASE_SIZE * speed if self.direction else - main.CASE_SIZE * speed
        if self.rect.left > main.WINDOW_SIZE[0]:
            self.kill()
