import math
from pygame import Vector3

from src.MeshSystem.WorldFace import WorldFace


class VectorMath:
    @staticmethod
    def dot(v1, v2):
        """
        Returns dot product of the given two vectors
        @param v1: 1st vector
        @type v1: Vector3 or Vector2
        @param v2: 2nd vector
        @type v2: Vector3 or Vector2
        @return: Dot product of two vectors
        @rtype: float
        """
        return sum((a * b) for a, b in zip(v1, v2))

    @staticmethod
    def length(v):
        """
        Returns the length of the given vector
        @type v: Vector3 or Vector2
        @param v: Vector to calculate length
        @rtype: float
        @return: Length of the vector
        """
        return math.sqrt(VectorMath.dot(v, v))

    # W radianach!!
    @staticmethod
    def unsigned_angle(v1, v2):
        """
        Returns the unsigned angle between two vectors
        @param v1: 1st vector
        @type v1: Vector3 or Vector2
        @param v2: 2nd vector
        @type v2: Vector3 or Vector2

        @rtype: float
        @return: Unsigned angle between two vectors in radians
        """
        return math.acos(VectorMath.dot(v1, v2) / (VectorMath.length(v1) * VectorMath.length(v2)))

    @staticmethod
    def normalize_vector(vec):
        """
        Normalizes the given vector so all lengths sum up to 1
        @param vec: Vector to normalize

        @rtype: Vector3 or Vector2
        @return: Normalized vector
        """
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
