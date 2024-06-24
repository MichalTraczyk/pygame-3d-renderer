from pygame import Color

from src.MeshSystem.Mesh import Mesh


class Primitives:

    @staticmethod
    def generate_box():
        mesh = Mesh(
            [(-0.5, 0, -0.5), (-0.5, 1, -0.5), (0.5, 1, -0.5), (0.5, 0, -0.5)
                , (-0.5, 0, 0.5), (-0.5, 1, 0.5), (0.5, 1, 0.5), (0.5, 0, 0.5)],
            [(0, 1, 2), (2, 3, 0), (4, 5, 1), (0, 4, 1), (2, 6, 7), (2, 7, 3)
                , (0, 3, 7), (7, 4, 0), (7, 5, 4), (7, 6, 5), (1, 5, 2), (5, 6, 2)])
        mesh.set_color(Color(255, 255, 255))
        return mesh
        pass

    @staticmethod
    def generate_pyramid():
        mesh = Mesh(
            [(0.5, 0, 1.75), (-0.5, 0, 1.75), (0, 0, 0), (0, 1, 1.05)],
            [(0, 2, 1), (0, 1, 3), (1, 2, 3), (0, 3, 2)])
        mesh.set_color(Color(255, 255, 255))
        return mesh

    @staticmethod
    def generate_rotated_pyramid():
        mesh = Mesh(
            [(0.5, 0, 0), (-0.5, 0, 0), (0, 0, 1.75), (0, 1, 0.7)],
            [(0, 2, 1), (0, 1, 3), (1, 2, 3), (0, 3, 2)])
        mesh.set_color(Color(255, 255, 255))
        return mesh

    @staticmethod
    def generate_diamond():
        mesh = Mesh(
            [(0.5, 0, 1.75), (-0.5, 0, 1.75), (0, 0, 0), (0, 1, 1.05), (0, -1, 1.05)],
            [(0, 1, 3), (1, 2, 3), (0, 3, 2), (1, 0, 4), (2, 1, 4), (2, 4, 0)])
        mesh.set_color(Color(255, 255, 255))
        return mesh

    @staticmethod
    def generate_plane(size: int, space: float = 1):
        offset = -size * space / 2
        if size <= 0 or space <= 0:
            raise ValueError('Size and space can not be negative or equal to zero!')
        faces = []
        for i in range(size * (size+1)-1):
            faces.append((i, i + size + 1, i + 1))
            faces.append((i + size + 1, i + size + 2, i + 1))
        # for z in range(size - 1):
        #   for x in range(size - 1):
        #      faces.append((x, (z + 1) * size + x, x + 1))
        #     faces.append(((z + 1) * size + x, (z + 1) * size + x + 1, x + 1))

        size += 1
        vertices = []
        for i in range(size * size):
            x = i % size
            z = int(i / size)
            vertices.append((space * x + offset, 0, space * z + offset))

        mesh = Mesh(vertices, faces)
        mesh.set_color(Color(255, 255, 255))
        return mesh
