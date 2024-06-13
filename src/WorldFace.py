from pygame import Vector3


class WorldFace:  # face jako kolekcja 3 wektorów w world position
    def __init__(self, v1: Vector3, v2: Vector3, v3: Vector3):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3

    def vectors(self):
        return self.v1, self.v2, self.v3
