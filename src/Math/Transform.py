import math

from pygame import Vector3, Vector2


class Transform:
    def __init__(self, position=Vector3(0, 0, 0), rotation=0):
        super().__init__()
        self.__parent: Transform = None
        self.__localPosition: Vector3 = Vector3(position)
        self.__localRotation: float = rotation

    def set_parent(self, parent):
        """
        Sets parent to this transform
        @param parent: Parent transform
        @type parent: Transform
        """
        self.__parent = parent
    def get_parent(self):
        """
        Returns parent transform of this transform
        @return: Transform parent
        @rtype: Transform
        """
        return self.__parent
    def get_position(self):
        """
        Returns world space position of the object
        @return: World space position of the object
        @rtype: Vector3
        """
        if self.__parent is None:
            return Vector3(self.__localPosition)
        else:
            return self.__parent.transform_point(self.__localPosition)

    def move(self, vector: Vector3):
        """
        Moves object by the given vector in world space
        @param vector: Move vector
        @type vector: Vector3
        """
        self.set_position(self.get_position() + vector)

    def get_rotation(self):
        """
        Returns world space rotation of the object
        @return: World space rotation
        @rtype: float
        """
        if self.__parent is None:
            return self.__localRotation
        else:
            self.__parent.get_rotation() + self.__localRotation

    def get_local_position(self):
        """
        Returns local position of the object
        @return: Local position
        @rtype: Vector3
        """
        return Vector3(self.__localPosition)

    def get_local_rotation(self):
        """
        Returns local rotation of the object
        @return: Local rotation
        @rtype: float
        """
        return self.__localRotation

    def rotate(self, rot: float):
        """
        Rotates object by the given angle
        @type rot: float
        @param rot: Angle
        """
        self.__localRotation += rot

    def set_position(self, pos: Vector3):
        """
        Sets the world position
        @param pos: Target world position
        @type pos: Vector3
        """
        if self.__parent is None:
            self.__localPosition = Vector3(pos)
        else:
            self.__localPosition = self.__parent.inverse_transform_point(pos)

    def set_local_position(self, pos: Vector3):
        """
        Sets the local position
        @param pos: Target local position
        @type pos: Vector3
        """
        self.__localPosition = Vector3(pos)

    def set_local_rotation(self, rot: float):
        """
        Sets the local rotation
        @param rot: Target rotation angle
        @type rot: float
        """
        self.__localRotation = rot

    def get_forward_vector(self):
        """
        Returns the vector in which object is facing
        @rtype: Vector3
        @return: Forward vector
        """
        return Vector3(math.sin(math.radians(self.__localRotation)), 0,
                       math.cos(math.radians(self.__localRotation))).normalize()

    # local position to world
    def transform_point(self, vector):
        """
        Return the local position of the given world space vector
        @param vector: World position
        @type vector: Vector3

        @rtype: Vector3
        @return: Local position
        """
        if vector.x == 0 and vector.z == 0:
            return self.get_position() + vector
        anglediff = Vector2(0, 1).angle_to(Vector2(vector.x, vector.z))
        anglediff += self.__localRotation
        anglediff = math.radians(anglediff)
        dist = math.sqrt(vector.x * vector.x + vector.z * vector.z)
        x = math.sin(anglediff) * dist
        z = math.cos(anglediff) * dist
        r = Vector3(x, vector.y, z)
        return self.get_position() + r

    # world position to local
    def inverse_transform_point(self, vector):
        """
        Return the world position of the given local vector
        @type vector: Vector3
        @param vector: Local position
        @rtype: Vector3
        @return: World position of point in this transform local space
        """
        localDiff = Vector2(vector.x - self.__localPosition.x, vector.z - self.__localPosition.z)
        angle = -Vector2(0, 1).angle_to(localDiff)
        angle -= self.__localRotation
        angle = math.radians(angle)
        dist = math.sqrt(localDiff.x * localDiff.x + localDiff.y * localDiff.y)
        x = math.sin(angle) * dist
        y = math.cos(angle) * dist
        return Vector3(x, vector.y - self.__localPosition.y, y)
