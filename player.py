import pygame as pg
import constants as const

class Buffer(object):
    def __init__(self, unit):
        super().__init__()
        self.val = 0 # value stored in the buffer
        self.unit = unit # "one" in the buffer corresponds to one unit

    def add(self, value):
        self.val += value

    def consume(self):
        if (self.val < 0):
            self.val += 1
            return - self.unit
        elif (self.val > 0):
            self.val -= 1
            return self.unit
        return 0

    def value(self):
        return self.val * self.unit

class Player(pg.sprite.Sprite):
    buffer_y = Buffer(const.CASE_SIZE / const.MOVE_STEPS)
    buffer_x = Buffer(const.CASE_SIZE / const.MOVE_STEPS)
    jmp = 0
    angle = 0
    SCROLL_STOP = const.HEIGHT - 5

    def __init__(self, image_path: str):
        super().__init__()
        self.image = pg.image.load(image_path + "chicken.png")
        self.image = pg.transform.scale(self.image, (36, 36))
        self.src_image = self.image
        self.is_alive = True

        self.mask = pg.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.x = const.CASE_SIZE * 7 + 2
        self.y = const.CASE_SIZE * 17 + 2
        self.rect.topleft = (self.x, self.y)

    def update(self, car_group):
        self.check_collision(car_group)
        offset = 0
        self.x += self.buffer_x.consume()
        self.y += self.buffer_y.consume()
        if (self.jmp != 0):
            factor = 1 + (const.MOVE_STEPS - abs(self.jmp - const.MOVE_STEPS)) / (const.MOVE_STEPS * 10)
            self.image = pg.transform.scale(self.src_image, (36 * factor, 36 * factor))
            offset = (36 * factor - 36) / 2
            self.jmp += 1
        if (self.jmp == 2 * const.MOVE_STEPS):
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
        if (not blocked and (0 <= self.x/const.CASE_SIZE + dx < const.WIDTH) and (self.SCROLL_STOP <= self.y/const.CASE_SIZE - dy < const.HEIGHT)):
            self.buffer_x.add(dx * const.MOVE_STEPS)
            self.buffer_y.add(- dy * const.MOVE_STEPS)
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
        case_x = self.get_position()[0]
        if 0 < case_x < const.WIDTH - 1 and pg.sprite.spritecollide(self, car_group, False, pg.sprite.collide_mask):
            self.is_alive = False
    
    def get_position(self):
        return (int((self.x + self.buffer_x.value()) / 40), int((self.y + self.buffer_y.value()) / 40))