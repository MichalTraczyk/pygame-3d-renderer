from src.MeshSystem import Mesh
from pygame import Vector3

class OBJFileReader:
    @staticmethod
    def read_file(filepath):
        vertices = []
        faces = []
        with open(filepath, 'r') as file:
            for line in file:
                if line.startswith('v '):
                    vertices.append(OBJFileReader.parse_vertex(line))
                elif line.startswith('f '):
                    faces.append(OBJFileReader.parse_face(line))
        return vertices, faces

    @staticmethod
    def parse_vertex(line):
        parts = line.strip().split()
        return Vector3(float(parts[1]), float(parts[2]), float(parts[3]))

    @staticmethod
    def parse_face(line):
        parts = line.strip().split()
        return (int(parts[1]), int(parts[2]), int(parts[3]))

    @staticmethod
    def create_mesh_from_obj(filepath):
        vertices, faces = OBJFileReader.read_file(filepath)
        return Mesh(vertices, faces)
