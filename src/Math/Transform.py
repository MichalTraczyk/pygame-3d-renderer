import math

from pygame import Vector3, Vector2

from src.Math.VectorMath import VectorMath


class Transform:
    def __init__(self, position=Vector3(0, 0, 0), rotation=0):
        super().__init__()
        self.__parent: Transform = None
        self.__localPosition: Vector3 = Vector3(position)
        self.__localRotation: float = rotation

    def GetPosition(self):
        if self.__parent is None:
            return Vector3(self.__localPosition)
        else:
            self.__parent.TransformPoint(self.__localPosition)

    def Move(self, vector: Vector3):
        self.SetPosition(self.GetPosition() + vector)

    def GetRotation(self):
        if self.__parent is None:
            return self.__localRotation
        else:
            self.__parent.GetRotation() + self.__localRotation

    def GetLocalPosition(self):
        return Vector3(self.__localPosition)

    def GetLocalRotation(self):
        return self.__localRotation

    def Rotate(self, rot: float):
        self.__localRotation += rot

    def SetPosition(self, pos: Vector3):
        if self.__parent is None:
            self.__localPosition = Vector3(pos)
        else:
            self.__localPosition = self.__parent.InverseTransformPoint(pos)

    def SetRotation(self, rot: float):
        self.__localRotation = rot

    def SetLocalPosition(self, pos: Vector3):
        self.__localPosition = Vector3(pos)

    def SetLocalRotation(self, rot: float):
        self.__localRotation = rot

    def GetForwardVector(self):
        return Vector3(math.sin(math.radians(self.__localRotation)),0,
                       math.cos(math.radians(self.__localRotation))).normalize()

    # local position to world
    def TransformPoint(self, vector):
        if(vector.x == 0 and vector.z == 0):
            return self.GetPosition() + vector
        anglediff =Vector2(0, 1).angle_to(Vector2(vector.x, vector.z))
        anglediff += self.__localRotation
        anglediff = math.radians(anglediff)
        dist = math.sqrt(vector.x * vector.x + vector.z * vector.z)
        x = math.sin(anglediff) * dist
        z = math.cos(anglediff) * dist
        r = Vector3(x, vector.y, z)
        return self.GetPosition() + r

    # world position to local
    def InverseTransformPoint(self, vector):
        localDiff = Vector2(vector.x - self.__localPosition.x, vector.z - self.__localPosition.z)
        angle = -Vector2(0, 1).angle_to(localDiff)
        angle -= self.__localRotation
        angle = math.radians(angle)
        dist = math.sqrt(localDiff.x * localDiff.x + localDiff.y * localDiff.y)
        x = math.sin(angle) * dist
        y = math.cos(angle) * dist
        return Vector3(x, vector.y - self.__localPosition.y, y)
