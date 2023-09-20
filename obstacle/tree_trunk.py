from obstacle.obstacle import Obstacle


class TreeTrunk(Obstacle):
    def __init__(self, x, y):
        self.tree_trunk_image = r".\images\trunk.png"
        super().__init__(x, y, self.tree_trunk_image)
