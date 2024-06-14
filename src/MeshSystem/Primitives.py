from pygame import Color

from src.MeshSystem.Mesh import Mesh


class Primitives:

    @staticmethod
    def generate_box():
        mesh = Mesh(
            [(-0.5, 0, 0), (-0.5, 1, 0), (0.5, 1, 0), (0.5, 0, 0)
                , (-0.5, 0, 1), (-0.5, 1, 1), (0.5, 1, 1), (0.5, 0, 1)],
            [(0, 1, 2), (2, 3, 0), (4, 5, 1), (1, 0, 4), (2, 6, 7), (6, 7, 5)
                , (0, 3, 7), (7, 4, 0), (5, 4, 7), (7, 6, 5), (1, 5, 2), (5, 6, 2)])
        mesh.set_color(Color(255, 255, 255))
        return mesh
        pass

    @staticmethod
    def generate_pyramid():
        mesh = Mesh(
            [(0.5, 0, 0), (-0.5, 0, 0), (0, 0, 1.75), (0, 1, 0, 7)],
            [(0, 2, 1), (0, 1, 3), (1, 2, 3), (0, 3, 2)])
        mesh.set_color(Color(255, 255, 255))
        return mesh
