from src.MeshSystem import Mesh
from pygame import Vector3

class OBJFileReader:
    @staticmethod
    def read_file(file_path):

        """
        converting OBJ file to mesh object
        @param file_path:
        @return: vertices, faces : list of vertices and faces to create mesh object
        """
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
