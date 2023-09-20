import pygame as pg

class Player:
    MOVE_STEPS = 8
    buffer_x, buffer_y = 0, 0
    pos_x, pos_y = 240, 520
    jmp = 0
    angle = 0

    def __init__(self):
        self.image = pg.image.load("chicken.png")
        self.image = pg.transform.scale(self.image, (40, 40))

    def draw(self, screen):
        img = self.image
        offset = 0
        # X animation
        if (self.buffer_x < 0):
            self.pos_x -= 40 / self.MOVE_STEPS
            self.buffer_x += 1
        elif (self.buffer_x > 0):
            self.pos_x += 40 / self.MOVE_STEPS
            self.buffer_x -= 1
        # Y animation
        if (self.buffer_y < 0):
            self.pos_y -= 40 / self.MOVE_STEPS
            self.buffer_y += 1
        elif (self.buffer_y > 0):
            self.pos_y += 40 / self.MOVE_STEPS
            self.buffer_y -= 1
        # Jump animation
        if (self.jmp != 0):
            factor = 1 + (self.MOVE_STEPS - abs(self.jmp - self.MOVE_STEPS)) / (self.MOVE_STEPS * 10)
            img = pg.transform.scale(self.image, (40 * factor, 40 * factor))
            offset = (40 * factor - 40) / 2
            self.jmp += 1
        if (self.jmp == 2 * self.MOVE_STEPS):
            self.jmp = 0
        screen.blit(img, (self.pos_x - offset, self.pos_y - offset))

    def get_pos(self):
        '''
        Retourne la position du joueur en nombre de cases
        '''
        return (int(self.pos_x/40), int(self.pos_y/40))
    
    def pos_to_angle(self, dx, dy):
        if (dy == 0):
            return -90 if dx > 0 else 90
        else:
            return 0 if dy > 0 else 180

    def move(self, dx: int, dy: int, blocked: bool = False):
        '''
        dx : Nombre de cases sur l'axe x [-1, 1]
        dy : Nombre de cases sur l'axe y [-1, 1]
        blocked : Si True, le joueur ne sera pas déplacé
        '''
        if (not blocked):
            self.buffer_x += dx * self.MOVE_STEPS
            self.buffer_y -= dy * self.MOVE_STEPS
        new_angle = self.pos_to_angle(dx, dy)
        if (self.angle != new_angle):
            self.image = pg.transform.rotate(self.image, - self.angle + new_angle)
            self.angle = new_angle
        if (self.jmp == 0):
            self.jmp = 1