import math
from pygame import Vector3

from src.MeshSystem.WorldFace import WorldFace


class VectorMath:
    @staticmethod
    def dot(v1, v2):
        return sum((a * b) for a, b in zip(v1, v2))

    @staticmethod
    def length(v):
        return math.sqrt(VectorMath.dot(v, v))

    # W radianach!!
    @staticmethod
    def unsigned_angle(v1, v2):
        return math.acos(VectorMath.dot(v1, v2) / (VectorMath.length(v1) * VectorMath.length(v2)))

    @staticmethod
    def normalize_vector(vec):
        return vec / VectorMath.length(vec)

    @staticmethod
    def face_normal(face: WorldFace):
        a = VectorMath.normalize_vector(face.v1 - face.v2)
        b = VectorMath.normalize_vector(face.v3 - face.v2)
        x = a.y * b.z - a.z * b.y
        y = a.z * b.x - a.x * b.z
        z = a.x * b.y - a.y * b.x
        return VectorMath.normalize_vector(Vector3(x, y, z))

    @staticmethod
    def face_middle(face: WorldFace):
        x = face.v1.x + face.v2.x + face.v3.x
        y = face.v1.y + face.v2.y + face.v3.y
        z = face.v1.z + face.v2.z + face.v3.z
        return Vector3(x, y, z) / 3
