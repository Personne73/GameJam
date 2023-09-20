from obstacle.obstacle import Obstacle


class Void(Obstacle):
    def __init__(self, x, y):
        self.void = r".\images\void.png"
        super().__init__(x, y, self.void)
