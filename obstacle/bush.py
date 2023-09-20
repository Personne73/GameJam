from obstacle.obstacle import Obstacle


class Bush(Obstacle):
    def __init__(self, x, y):
        self.bush = r".\images\bush.png"
        super().__init__(x, y, self.bush)
