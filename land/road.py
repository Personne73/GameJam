import pygame as pg
from car import Car
import random
import constants


class Road():
    next_car = 0
    last_car = None

    def __init__(self, type_terrain):
        super().__init__()
        self.type_terrain = type_terrain
        self.x = 1 * constants.CASE_SIZE
        self.y = 0
        self.direction = random.randint(0,1)
        self.cars = pg.sprite.Group()
        self.speed_factor = random.randint(-20, 20) / 100 + 1

    def update(self, car_group):
        if self.can_spawn_new_car():
            new_car = Car(constants.IMG_PATH, self.direction, self.y, self.speed_factor)
            car_group.add(new_car)
            self.cars.add(new_car)
            self.next_car = random.randint(new_car.rect.w + constants.CASE_SIZE, constants.WIDTH * constants.CASE_SIZE)
            self.next_car = new_car.x + self.next_car * (-1 if self.direction else 1)
            if self.last_car is None:
                new_car.x = random.randint(new_car.rect.w + constants.CASE_SIZE, (constants.WIDTH-4) * constants.CASE_SIZE) * (-1 if self.direction else 1)
            self.last_car = new_car

    def move(self, y):
        self.y = y
        for car in self.cars.sprites():
            car.rect.top = y

    def kill(self):
        for car in self.cars.sprites():
            car.kill()

    def can_spawn_new_car(self):
        if self.last_car is None:
            return True
        elif self.direction:
            return self.last_car.x < self.next_car
        else:
            return self.last_car.x > self.next_car