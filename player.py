import pygame as pg
import constants

class Buffer(object):
    def __init__(self, unit):
        super().__init__()
        self.value = 0 # value stored in the buffer
        self.unit = unit # "one" in the buffer corresponds to one unit

    def add(self, value):
        self.value += value

    def consume(self):
        if (self.value < 0):
            self.value += 1
            return - self.unit
        elif (self.value > 0):
            self.value -= 1
            return self.unit
        return 0

class Player(pg.sprite.Sprite):
    MOVE_STEPS = 8
    buffer_y = Buffer(constants.CASE_SIZE / MOVE_STEPS)
    buffer_x = Buffer(constants.CASE_SIZE / MOVE_STEPS)
    jmp = 0
    angle = 0
    ligne_scroll_stop = constants.HEIGHT - 5

    def __init__(self, image_path: str):
        super().__init__()
        self.image = pg.image.load(image_path + "chicken.png")
        self.image = pg.transform.scale(self.image, (36, 36))
        self.src_image = self.image
        self.is_alive = True

        self.mask = pg.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.x = constants.CASE_SIZE * 6 + 2
        self.y = self.ligne_scroll_stop * constants.CASE_SIZE + 2
        self.rect.topleft = (self.x, self.y)

    def update(self, car_group):
        self.check_collision(car_group)
        offset = 0
        self.x += self.buffer_x.consume()
        self.y += self.buffer_y.consume()
        if (self.jmp != 0):
            factor = 1 + (self.MOVE_STEPS - abs(self.jmp - self.MOVE_STEPS)) / (self.MOVE_STEPS * 10)
            self.image = pg.transform.scale(self.src_image, (36 * factor, 36 * factor))
            offset = (36 * factor - 36) / 2
            self.jmp += 1
        if (self.jmp == 2 * self.MOVE_STEPS):
            self.jmp = 0
        
        self.mask = pg.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x - offset, self.y - offset)
        
    def move(self, dx: int, dy: int, blocked: bool = False):
        '''
        dx : Nombre de cases sur l'axe x [-1, 1]
        dy : Nombre de cases sur l'axe y [-1, 1]
        blocked : Si True, le joueur ne sera pas déplacé
        '''
        print("x :", self.x, "y :", self.y)
        print((self.x // 40, self.y // 40))
        if (not blocked and (0 <= self.x/constants.CASE_SIZE + dx < constants.WIDTH) and (self.ligne_scroll_stop <= self.y/constants.CASE_SIZE - dy < constants.HEIGHT)):
            self.buffer_x.add(dx * self.MOVE_STEPS)
            self.buffer_y.add(- dy * self.MOVE_STEPS)
        new_angle = self.pos_to_angle(dx, dy)
        if (self.angle != new_angle):
            self.src_image = pg.transform.rotate(self.src_image, - self.angle + new_angle)
            self.angle = new_angle
        if (self.jmp == 0):
            self.jmp = 1

    def pos_to_angle(self, dx, dy):
        if (dy == 0):
            return -90 if dx > 0 else 90
        else:
            return 0 if dy > 0 else 180
        
    def check_collision(self, car_group):
        case_x = self.x / constants.CASE_SIZE
        if 0 < case_x < constants.WIDTH - 1 and pg.sprite.spritecollide(self, car_group, False, pg.sprite.collide_mask):
            self.is_alive = False
    
    def get_position(self):
        return (int(self.x // 40), int(self.y // 40))
    
    # def isBlocked(self, terrain):
    #     if terrain[]