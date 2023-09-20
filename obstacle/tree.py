from obstacle.obstacle import Obstacle


class Tree(Obstacle):
    def __init__(self, x, y):
        self.tree_image = r".\images\tree.png"
        super().__init__(x, y, self.tree_image)







