from src.MeshSystem import Mesh
from pygame import Vector3

class OBJFileReader:
    @staticmethod
    def read_file(file_path):
        vertices = []
        faces = []
        with open(file_path, 'r') as file:
            for line in file:
                if line.startswith('v '):
                    parts = line.strip().split()
                    vertices.append(Vector3(float(parts[1]), float(parts[2]), float(parts[3])))
                elif line.startswith('f '):
                    parts = line.strip().split()
                    face = (int(parts[1].split('/')[0]) - 1,
                            int(parts[2].split('/')[0]) - 1,
                            int(parts[3].split('/')[0]) - 1)
                    faces.append(face)
        return vertices, faces

    @staticmethod
    def parse_vertex(line):
        parts = line.strip().split()
        return Vector3(float(parts[1]), float(parts[2]), float(parts[3]))

    @staticmethod
    def create_mesh_from_obj(filepath):
        vertices, faces = OBJFileReader.read_file(filepath)
        return Mesh(vertices, faces)
