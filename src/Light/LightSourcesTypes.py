from pygame import Vector3, Color

from src.Light.LightSource import LightSource
from src.Math.VectorMath import VectorMath
from src.MeshSystem.WorldFace import WorldFace


class DirectionalLight(LightSource):

    def __init__(self, pos: Vector3, direction: Vector3, intensity: float, color: Color):
        super().__init__(pos, intensity, color)
        self.direction = direction

    def get_light_level(self, face: WorldFace):
        normal = VectorMath.face_normal(face)
        directiontocamera = -VectorMath.normalize_vector(VectorMath.face_middle(face))  # do sprawdzenia

        dot = VectorMath.Dot(normal, directiontocamera)
        if dot < 0:
            dot = 0

        value = self.intensity * dot
        r = int(self.color.r * value)
        g = int(self.color.g * value)
        b = int(self.color.b * value)

        return Color(r, g, b)


class PointLight(LightSource):
    def __init__(self, pos: Vector3, intensity: float, color: Color):
        super().__init__(pos, intensity, color)

    def get_light_level(self, face: WorldFace):
        normal = VectorMath.face_normal(face)
        middle = VectorMath.face_middle(face)
        direction = VectorMath.normalize_vector(self.get_position() - middle)
        distance = VectorMath.Length(VectorMath.face_middle(face) - self.get_position())
        dot = VectorMath.Dot(normal, direction)
        if dot < 0:
            dot = 0
        value = self.intensity * dot / distance
        if value > 1:
            value = 1
        r = int(self.color.r * value)
        g = int(self.color.g * value)
        b = int(self.color.b * value)

        return Color(r, g, b)


class SkyboxLight(LightSource):
    def __init__(self, pos: Vector3, intensity: float, color: Color):
        super().__init__(pos, intensity, color)

    def get_light_level(self, face: WorldFace):
        value = self.intensity
        r = int(self.color.r * self.intensity)
        g = int(self.color.g * self.intensity)
        b = int(self.color.b * self.intensity)

        return Color(r, g, b)
