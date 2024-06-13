import math
from pygame import Vector3


class VectorMath:
    @staticmethod
    def Dot(v1, v2):
        return sum((a * b) for a, b in zip(v1, v2))

    @staticmethod
    def Length(v):
        return math.sqrt(VectorMath.Dot(v, v))

    # W radianach!!
    @staticmethod
    def UnsignedAngle(v1, v2):
        return math.acos(VectorMath.Dot(v1, v2) / (VectorMath.Length(v1) * VectorMath.Length(v2)))

    @staticmethod
    def normalize_vector(vec):
        return vec / VectorMath.Length(vec)

    @staticmethod
    def face_normal(v1: Vector3, v2: Vector3, v3: Vector3):
        a = v1 - v2
        b = v3 - v2
        x = a.y * b.z - a.z * b.y
        y = a.z * b.x - a.x * b.z
        z = a.x * b.y - a.y * b.x
        return Vector3(x, y, z)
