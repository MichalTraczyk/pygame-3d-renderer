import math


class VectorMath:
    @staticmethod
    def Dot(v1, v2):
      return sum((a*b) for a, b in zip(v1, v2))

    @staticmethod
    def Length(v):
      return math.sqrt(VectorMath.Dot(v, v))

    #W radianach!!
    @staticmethod
    def UnsignedAngle(v1, v2):
      return math.acos(VectorMath.Dot(v1, v2) / (VectorMath.Length(v1) * VectorMath.Length(v2)))