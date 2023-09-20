from obstacle.obstacle import Obstacle


class Rock(Obstacle):
    def __init__(self, x, y, rock_image):
        super().__init__(x, y, rock_image)
