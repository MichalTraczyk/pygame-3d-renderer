from pygame import Vector3


class Mesh:

    def __init__(self, vertices: [Vector3], faces: [(int, int, int)]):
        self.vertices = vertices
        self.faces = faces

    def get_faces(self):  # faces as vertex positions in local space
        fcs = []
        for f in self.faces:
            v1 = self.vertices[f[0]]
            v2 = self.vertices[f[1]]
            v3 = self.vertices[f[2]]
            fcs.append((v1, v2, v3))
