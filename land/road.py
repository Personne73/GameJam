import pygame as pg
from car import Car
import random
import main


class Road():
    next_car = 0
    last_car = None

    def __init__(self, image_path: str):
        super().__init__()
        self.x = 1 * main.CASE_SIZE
        self.y = main.CASE_SIZE * 8
        self.direction = random.randint(0,1)
        self.image_path = image_path
        self.cars = pg.sprite.Group()
        self.speed_factor = random.randint(-20, 20) / 100 + 1

    def update(self, car_group):
        if self.can_spawn_new_car():
            new_car = Car(self.image_path, self.direction, self.y, self.speed_factor)
            car_group.add(new_car)
            self.cars.add(new_car)
            self.next_car = random.randint(new_car.rect.w + main.CASE_SIZE, main.WIDTH * main.CASE_SIZE)
            self.next_car = new_car.x + self.next_car * (-1 if self.direction else 1)
            if self.last_car is None:
                new_car.x = random.randint(new_car.rect.w + main.CASE_SIZE, (main.WIDTH-4) * main.CASE_SIZE) * (-1 if self.direction else 1)
            self.last_car = new_car

    def move(self, dy):
        self.y += dy
        for car in self.cars.sprites():
            car.rect.top += dy

    def can_spawn_new_car(self):
        if self.last_car is None:
            return True
        elif self.direction:
            return self.last_car.x < self.next_car
        else:
            return self.last_car.x > self.next_car