import math

from pygame import Vector3, Vector2

from src.Math.VectorMath import VectorMath


class Transform:
    def __init__(self, position=Vector3(0, 0, 0), rotation=0):
        self.__parent: Transform = None
        self.__localPosition = Vector3(position)
        self.__localRotation = rotation

    def GetPosition(self):
        if self.__parent == None:
            return Vector3(self.__localPosition)
        else:
            self.__parent.TransformPoint(self.__localPosition)

    def GetRotation(self):
        if self.__parent == None:
            return self.__localRotation
        else:
            self.__parent.GetRotation() + self.__localRotation

    def GetLocalPosition(self):
        return Vector3(self.__localPosition)

    def GetLocalRotation(self):
        return self.__localRotation

    def Rotate(self, rot):
        self.__localRotation += rot

    def SetPosition(self):
        pass

    def SetRotation(self):
        pass

    def SetLocalPosition(self, pos):
        self.__localPosition = Vector3(pos)

    def SetLocalRotation(self, rot):
        self.__localRotation = rot

    def GetForwardVector(self):
        return Vector2(math.sin(math.radians(self.__localRotation)),
                       math.cos(math.radians(self.__localRotation))).normalize()

    # local position to world
    def TransformPoint(self, vector):
        anglediff = VectorMath.UnsignedAngle(Vector2(0, 1), vector)
        anglediff += math.radians(self.__localRotation)
        dist = math.sqrt(vector.x * vector.x + vector.y * vector.y)
        x = math.sin(anglediff) * dist
        y = math.cos(anglediff) * dist
        r = Vector3(x, y, 0)
        return self.GetPosition() + r

    # world position to local
    def InverseTransformPoint(self, vector):
        localDiff = Vector2(vector.x - self.__localPosition.x, vector.y - self.__localPosition.y)
        angle = -Vector2(0, 1).angle_to(localDiff)
        angle -= self.__localRotation
        angle = math.radians(angle)
        dist = math.sqrt(localDiff.x * localDiff.x + localDiff.y * localDiff.y)
        x = math.sin(angle) * dist
        y = math.cos(angle) * dist
        return Vector3(x, y, 0)
