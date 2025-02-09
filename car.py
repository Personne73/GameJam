import pygame as pg
import random
import constants

class Car(pg.sprite.Sprite):
    SKINS = []
    def __init__(self, image_path: str, direction: bool, y: int, speed_factor: int):
        super().__init__()
        self.direction = direction
        self.speed_factor = speed_factor

        # Load the images only once
        if Car.SKINS == []:
            Car.SKINS = [
                pg.image.load(image_path + "blue_car.png"),
                pg.image.load(image_path + "green_car.png"),
                pg.image.load(image_path + "orange_car.png"),
                pg.image.load(image_path + "pink_car.png"),
                pg.image.load(image_path + "red_car.png"),
                pg.image.load(image_path + "violet_car.png"),
                pg.image.load(image_path + "yellow_car.png"),
                pg.image.load(image_path + "blue_truck.png"),
                pg.image.load(image_path + "green_truck.png"),
                pg.image.load(image_path + "orange_truck.png"),
                pg.image.load(image_path + "red_truck.png")
            ]

        self.image = Car.SKINS[random.randint(0, len(Car.SKINS) - 1)]
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)
        self.rect.top = y
        if self.direction:
            self.image = pg.transform.rotate(self.image, 180)
            self.x = constants.WINDOW_SIZE[0]
        else:
            self.x = - self.rect.w
        self.rect.left = self.x

    def update(self, speed):
        speed *= self.speed_factor
        self.x -= constants.CASE_SIZE * speed if self.direction else - constants.CASE_SIZE * speed
        self.rect.left = self.x
        if self.x > constants.WINDOW_SIZE[0] or self.x < - self.rect.w:
            self.kill()
