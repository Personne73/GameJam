from obstacle.obstacle import Obstacle


class Rock(Obstacle):
    def __init__(self, x, y):
        self.rock_image = r".\images\rock.png"
        super().__init__(x, y, self.rock_image)
