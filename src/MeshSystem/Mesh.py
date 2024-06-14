from pygame import Vector3, Color


class Mesh:

    def __init__(self, vertices: [Vector3], faces: [(int, int, int)]):
        self.vertices = vertices  # jako lokalna pozycja vertexów
        self.faces = faces  # jako indeksy vertexów
        self.__color = Color(255, 255, 255)

    def get_faces(self):  # jako vertexy w local space
        fcs = []
        for f in self.faces:
            v1 = self.vertices[f[0]]
            v2 = self.vertices[f[1]]
            v3 = self.vertices[f[2]]
            fcs.append((v1, v2, v3))
        return fcs

    def set_color(self, color: Color):
        self.__color = color

    def get_rendered_color(self, light_level: float):
        return Color(0, 0, 0).lerp(self.__color, light_level)
