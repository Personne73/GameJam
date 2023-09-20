class Terrain(object):
    # 14x18 blocks, dont 2 de bordure en largeur
    def __init__(self):
        self.tableau = [[None for i in range(14)] for j in range(18)]

