class Terrain(object):
    def __init__(self):
        self.tableau = [[0 if i in [0, 13] else 1 for i in range(14)] for j in range(20)]